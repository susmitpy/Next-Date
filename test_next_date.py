#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:05:20 2020

@author: susmitvengurlekar
"""

import unittest
from next_date import next_date


class TestNextDate(unittest.TestCase):

    def test_one(self):
        self.assertEqual(next_date(date="2020/1/1"), "2020/1/2")

    def test_thirty_one(self):
        self.assertEqual(next_date(date="2020/1/31"), "2020/2/1")

    def test_feb_leap(self):
        self.assertEqual(next_date(date="2020/2/29"), "2020/3/1")

    def test_feb_non_leap(self):
        self.assertEqual(next_date(date="2019/2/28"), "2019/3/1")

    def test_thirty(self):
        self.assertEqual(next_date(date="2020/4/30"), "2020/5/1")

    def test_thirty_one_dec(self):
        self.assertEqual(next_date(date="2020/12/31"), "2021/1/1")


if __name__ == '__main__':
    unittest.main()
