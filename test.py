from __future__ import unicode_literals

import unittest
import collections

from torrent_parser import TorrentFileParser, parse_torrent_file


class Test(unittest.TestCase):
    TEST_FILENAME = 'test.torrent'

    def test_parse_torrent_file_use_shortcut(self):
        parse_torrent_file(self.TEST_FILENAME)

    def test_parse_torrent_file_use_class(self):
        with open(self.TEST_FILENAME, 'rb') as fp:
            TorrentFileParser(fp).parse()

    def test_parse_torrent_file_to_ordered_dict(self):
        data = parse_torrent_file(self.TEST_FILENAME, True)
        self.assertIsInstance(data, collections.OrderedDict)

        with open(self.TEST_FILENAME, 'rb') as fp:
            data = TorrentFileParser(fp, True).parse()
        self.assertIsInstance(data, collections.OrderedDict)

    def test_parse_correctness(self):
        data = parse_torrent_file(self.TEST_FILENAME)
        self.assertIn(['udp://tracker.publicbt.com:80/announce'],
                      data['announce-list'])
        self.assertEqual(data['creation date'], 1409254242)

    def test_parse_two_times(self):
        with open(self.TEST_FILENAME, 'rb') as fp:
            parser = TorrentFileParser(fp)
            data = parser.parse()
            self.assertIn(['udp://tracker.publicbt.com:80/announce'],
                          data['announce-list'])
            self.assertEqual(data['creation date'], 1409254242)
            data = parser.parse()
            self.assertIn(['udp://tracker.publicbt.com:80/announce'],
                          data['announce-list'])
            self.assertEqual(data['creation date'], 1409254242)
