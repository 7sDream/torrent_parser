from __future__ import unicode_literals

import os.path
import unittest

from torrent_parser import TorrentFileParser, decode, parse_torrent_file


class TestHashField(unittest.TestCase):
    TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), "test_files")
    FILE = os.path.join(TEST_FILES_DIR, "utf8.encoding.error.torrent")

    def test_not_raise_exception_when_add_hash_fields(self):
        parse_torrent_file(self.FILE, hash_fields={"info_hash": (20, False)})
        with open(self.FILE, "rb") as f:
            TorrentFileParser(f).hash_field("info_hash").parse()
