from __future__ import unicode_literals

import unittest

from torrent_parser import encode


class TestEncode(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(encode(12345), b'i12345e')
