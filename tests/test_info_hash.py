from __future__ import unicode_literals

import binascii
import hashlib
import os.path
import unittest
from distutils.log import info

from torrent_parser import create_torrent_file, encode, parse_torrent_file


class TestInfoHash(unittest.TestCase):
    TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), "test_files")
    REAL_FILE = os.path.join(TEST_FILES_DIR, "xubuntu-22.04-desktop-amd64.iso.torrent")

    def test_info_hash_is_right(self):
        torrent = parse_torrent_file(self.REAL_FILE, hash_raw=True)
        info_bytes = encode(torrent["info"])
        info_hash = binascii.hexlify(hashlib.sha1(info_bytes).digest()).decode()
        # print(f"info_hash: {info_hash}")
        self.assertEqual(info_hash, "f435d2324f313bad7ff941633320fe4d1c9c3079")
