from __future__ import unicode_literals

import os.path
import unittest

from torrent_parser import (
    TorrentFileParser, parse_torrent_file, InvalidTorrentDataException
)


class TestDecodingError(unittest.TestCase):
    TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), 'test_files')
    FILE = os.path.join(TEST_FILES_DIR, 'utf8.encoding.error.torrent')

    def test_default_option_will_raise_exception(self):
        with self.assertRaises(InvalidTorrentDataException):
            parse_torrent_file(self.FILE)
        with self.assertRaises(InvalidTorrentDataException):
            with open(self.FILE, 'rb') as f:
                TorrentFileParser(f).parse()

    def test_not_raise_exception_when_use_ignore(self):
        parse_torrent_file(self.FILE, errors='ignore')
        with open(self.FILE, 'rb') as f:
            TorrentFileParser(f, errors='ignore').parse()
