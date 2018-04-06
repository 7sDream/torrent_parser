#!/usr/bin/env python
# coding: utf-8

"""
A .torrent file parser for both Python 2 and 3

Usage:

    data = parse_torrent_file(filename)

    # or

    with open(filename, 'rb') as f: # the binary mode 'b' is necessary
        data = TorrentFileParser(f).parse()
"""

from __future__ import print_function, unicode_literals

import argparse
import collections
import io
import json
import sys
import warnings

try:
    FileNotFoundError
except NameError:
    # Python 2 do not have FileNotFoundError, use IOError instead
    # noinspection PyShadowingBuiltins
    FileNotFoundError = IOError

try:
    # noinspection PyPackageRequirements
    from chardet import detect as _detect
except ImportError:
    def _detect(_):
        warnings.warn("No chardet module installed, encoding will be utf-8")
        return {'encoding': 'utf-8', 'confidence': 1}

__all__ = [
    'InvalidTorrentDataException',
    'parse_torrent_file',
    'TorrentFileParser',
]

__version__ = '0.1.4'


def detect(content):
    return _detect(content)['encoding']


class InvalidTorrentDataException(Exception):
    def __init__(self, pos, msg=None):
        msg = msg or "Invalid torrent format when read at pos {pos}"
        msg = msg.format(pos=pos)
        super(InvalidTorrentDataException, self).__init__(msg)


class __EndCls(object):
    pass


_END = __EndCls()


class TorrentFileParser(object):

    TYPE_LIST = 'list'
    TYPE_DICT = 'dict'
    TYPE_INT = 'int'
    TYPE_STRING = 'string'
    TYPE_END = 'end'

    LIST_INDICATOR = b'l'
    DICT_INDICATOR = b'd'
    INT_INDICATOR = b'i'
    END_INDICATOR = b'e'
    STRING_INDICATOR = b''

    TYPES = [
        (TYPE_LIST, LIST_INDICATOR),
        (TYPE_DICT, DICT_INDICATOR),
        (TYPE_INT, INT_INDICATOR),
        (TYPE_END, END_INDICATOR),
        (TYPE_STRING, STRING_INDICATOR),
    ]

    def __init__(self, fp, use_ordered_dict=False, encoding='utf-8'):
        """
        :param fp: a **binary** file-like object to parse,
          which means need 'b' mode when use built-in open function
        :param encoding: file content encoding, default utf-8, use 'auto' to
          enable charset auto detection ('chardet' package should be installed)
        :param use_ordered_dict: Use collections.OrderedDict as dict container
          default False, which mean use built-in dict
        """
        if getattr(fp, 'read', ) is None \
                or getattr(fp, 'seek') is None:
            raise ValueError('Argument fp needs a file like object')

        self._pos = 0
        self._encoding = encoding
        self._content = fp
        self._use_ordered_dict = use_ordered_dict

    def parse(self):
        """
        :return: the parse result
        :type: depends on ``use_ordered_dict`` option when init the parser
          see :any:`TorrentFileParser.__init__`
        """
        self._restart()
        data = self._next_element()

        try:
            c = self._read_byte(1, True)
            raise InvalidTorrentDataException(
                0, 'Expect EOF, but get [{}] at pos {}'.format(c, self._pos)
            )
        except EOFError:  # expect EOF
            pass

        if isinstance(data, dict):
            return data

        raise InvalidTorrentDataException('Outermost element is not a dict')

    def _read_byte(self, count=1, raise_eof=False):
        assert count >= 0
        gotten = self._content.read(count)
        if count != 0 and len(gotten) == 0:
            if raise_eof:
                raise EOFError()
            raise InvalidTorrentDataException(
                self._pos,
                'Unexpected EOF when reading torrent file'
            )
        self._pos += count
        return gotten

    def _seek_back(self, count):
        self._content.seek(-count, 1)
        self._pos = self._pos - count

    def _restart(self):
        self._content.seek(0, 0)
        self._pos = 0

    def _dict_items_generator(self):
        while True:
            k = self._next_element()
            if k is _END:
                return
            if k == 'pieces':
                v = self._next_hash()
            elif k == 'ed2k':
                v = self._next_hash(16, False)
            elif k == 'filehash':
                v = self._next_hash(20, False)
            else:
                v = self._next_element()
            if k == 'encoding':
                self._encoding = v
            yield k, v

    def _next_dict(self):
        data = collections.OrderedDict() if self._use_ordered_dict else dict()
        for key, element in self._dict_items_generator():
            data[key] = element
        return data

    def _list_items_generator(self):
        while True:
            element = self._next_element()
            if element is _END:
                return
            yield element

    def _next_list(self):
        return [element for element in self._list_items_generator()]

    def _next_int(self, end=END_INDICATOR):
        value = 0
        char = self._read_byte(1)
        neg = False
        while char != end:
            if not neg and char == b'-':
                neg = True
            elif not b'0' <= char <= b'9':
                raise InvalidTorrentDataException(self._pos - 1)
            else:
                value = value * 10 + int(char) - int(b'0')
            char = self._read_byte(1)
        return -value if neg else value

    def _next_string(self, decode=True):
        length = self._next_int(b':')
        raw = self._read_byte(length)
        if decode:
            encoding = self._encoding
            if encoding == 'auto':
                encoding = detect(raw)
            try:
                string = raw.decode(encoding)
            except UnicodeDecodeError as e:
                raise InvalidTorrentDataException(
                    self._pos - length + e.start,
                    "Fail to decode string at pos {pos} using " + e.encoding
                )
            return string
        return raw

    @staticmethod
    def __to_hex(v):
        return hex(ord(v) if isinstance(v, str) else v)[2:].rjust(2, str(0))

    def _next_hash(self, p_len=20, need_list=True):
        raw = self._next_string(decode=False)
        if len(raw) % p_len != 0:
            raise InvalidTorrentDataException(
                self._pos - len(raw), "Hash bit length not match at pos {pos}"
            )
        res = [
            ''.join([self.__to_hex(c) for c in h])
            for h in (raw[x:x+p_len] for x in range(0, len(raw), p_len))
        ]
        if len(res) == 0 and not need_list:
            return ''
        if len(res) == 1 and not need_list:
            return res[0]
        return res

    @staticmethod
    def _next_end():
        return _END

    def _next_type(self):
        for (element_type, indicator) in self.TYPES:
            indicator_length = len(indicator)
            char = self._read_byte(indicator_length)
            if indicator == char:
                return element_type
            self._seek_back(indicator_length)
        raise InvalidTorrentDataException(self._pos)

    def _type_to_func(self, t):
        return getattr(self, '_next_' + t)

    def _next_element(self):
        element_type = self._next_type()
        element = self._type_to_func(element_type)()
        return element


def parse_torrent_file(filename, use_ordered_dict=False):
    """
    Shortcut function for parse torrent object use TorrentFileParser

    :param string filename: torrent filename
    :param bool use_ordered_dict: see :any:`TorrentFileParser.__init__`
    :rtype: dict if ``use_ordered_dict`` is false,
      collections.OrderedDict otherwise
    """
    with open(filename, 'rb') as f:
        return TorrentFileParser(f, use_ordered_dict).parse()


def __main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', default='',
                        help='input file, will read form stdin if empty')
    parser.add_argument('--dict', '-d', action='store_true', default=False,
                        help='use built-in dict, default will be OrderedDict')
    parser.add_argument('--sort', '-s', action='store_true', default=False,
                        help='sort output json item by key')
    parser.add_argument('--indent', '-i', type=int, default=None,
                        help='json output indent for every inner level')
    parser.add_argument('--ascii', '-a', action='store_true', default=False,
                        help='ensure output json use ascii char, '
                             'escape other char use \\u')
    parser.add_argument('--coding', '-c', default='utf-8',
                        help='string encoding, default utf-8')
    parser.add_argument('--version', '-v', action='store_true', default=False,
                        help='print version and exit')
    args = parser.parse_args()

    if args.version:
        print(__version__)
        exit(0)

    try:
        if args.file == '':
            target_file = io.BytesIO(
                getattr(sys.stdin, 'buffer', sys.stdin).read()
            )
        else:
            target_file = open(args.file, 'rb')
    except FileNotFoundError:
        sys.stderr.write('File "{}" not exist\n'.format(args.file))
        exit(1)

    # noinspection PyUnboundLocalVariable
    data = TorrentFileParser(target_file, not args.dict, args.coding).parse()

    data = json.dumps(
        data, ensure_ascii=args.ascii,
        sort_keys=args.sort, indent=args.indent
    )

    print(data)


if __name__ == '__main__':
    __main()
