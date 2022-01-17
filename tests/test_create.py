from __future__ import unicode_literals

import collections
import hashlib
import io
import os.path
import unittest

from torrent_parser import BEncoder, TorrentFileCreator, TorrentFileParser


class TestCreate(unittest.TestCase):
    TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), "test_files")
    REAL_FILE = os.path.join(TEST_FILES_DIR, "real.torrent")
    REAL_FILE_V2 = os.path.join(TEST_FILES_DIR, "bittorrent-v2-test.torrent")

    def test_simple_create(self):
        data = collections.OrderedDict()
        data["a"] = 1
        data["b"] = 2
        self.assertEqual(BEncoder(data).encode(), b"d1:ai1e1:bi2ee")

    def test_same_output_if_no_edit(self):
        with open(self.REAL_FILE, "rb") as fp:
            in_data = fp.read()
            data = TorrentFileParser(io.BytesIO(in_data), True).parse()
            out_data = TorrentFileCreator(data).create_filelike()

            m1 = hashlib.md5()
            m1.update(in_data)
            m2 = hashlib.md5()
            m2.update(out_data.getbuffer())
            self.assertEqual(m1.digest(), m2.digest())

    def test_same_output_if_no_edit_v2(self):
        with open(self.REAL_FILE_V2, "rb") as fp:
            in_data = fp.read()
            data = TorrentFileParser(io.BytesIO(in_data), True).parse()
            out_data = TorrentFileCreator(data).create_filelike()

            m1 = hashlib.md5()
            m1.update(in_data)
            m2 = hashlib.md5()
            m2.update(out_data.getbuffer())
            self.assertEqual(m1.digest(), m2.digest())

    def test_dont_need_dict_outmost(self):
        data = 123456
        self.assertEqual(BEncoder(data).encode(), b"i123456e")
