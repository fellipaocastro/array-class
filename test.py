#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import
import unittest

from array_class import ArrayClass


class ArrayClassTestCase(unittest.TestCase):
    def setUp(self):
        self.original_array = [10, 3, 8, 2, 8, 17]

    def test_eliminate_duplicate(self):
        """
        ArrayClass.eliminate_duplicate should return a list without duplicate elements
        """
        array_object = ArrayClass(self.original_array)
        expected_array = [8, 17, 10, 3, 2]

        array_object.eliminate_duplicate()    

        self.assertEqual(array_object.array, expected_array)


if __name__ == '__main__':
    unittest.main()
