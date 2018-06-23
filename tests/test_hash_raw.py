from __future__ import unicode_literals

import os.path
import unittest

from torrent_parser import decode, encode


class TestHashRaw(unittest.TestCase):
    TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), 'test_files')
    FILE = os.path.join(TEST_FILES_DIR, 'utf8.encoding.error.torrent')

    def test_hash_raw_decode(self):
        data = b'd4:hash4:\xAA\xBB\xCC\xDDe'
        res = decode(data, hash_fields={'hash': (4, False)}, hash_raw=False)
        self.assertEqual(res['hash'], 'aabbccdd')
        res = decode(data, hash_fields={'hash': (4, False)}, hash_raw=True)
        self.assertEqual(res['hash'], b'\xAA\xBB\xCC\xDD')

    def test_raw_bytes_encode(self):
        res = {'hash': b'\xAA\xBB\xCC\xDD'}
        data = encode(res)
        self.assertEqual(data, b'd4:hash4:\xAA\xBB\xCC\xDDe')
