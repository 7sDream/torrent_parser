from __future__ import unicode_literals

import unittest

from torrent_parser import decode


class TestDecode(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(decode(b'i12345e'), 12345)
