from __future__ import unicode_literals

import os.path
import unittest

from torrent_parser import InvalidTorrentDataException, TorrentFileParser, decode


class TestDecodingError(unittest.TestCase):
    TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), "test_files")
    FILE = os.path.join(TEST_FILES_DIR, "utf8.encoding.error.torrent")

    def test_default_option_will_raise_exception(self):
        with open(self.FILE, "rb") as f:
            with self.assertRaises(InvalidTorrentDataException):
                decode(f)

    def test_not_raise_exception_when_use_ignore(self):
        with open(self.FILE, "rb") as f:
            decode(f, errors="ignore")
