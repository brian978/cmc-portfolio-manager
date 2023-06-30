import unittest

from format_date import format_date


class FormatDateCase(unittest.TestCase):
    def test_it_converts_from_cg_to_cmc_format(self):
        date = '22 Sep 2022 07:10 AM UTC'
        expected = '2022-09-22T07:10:00.000Z'

        self.assertEqual(expected, format_date(date))
