#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import
import unittest

from array_class import ArrayClass


class ArrayClassTestCase(unittest.TestCase):
    def setUp(self):
        original_array = [10, 3, 8, 2, 8, 17]
        self.array_object = ArrayClass(original_array)

    def test___init__(self):
        """
        ArrayClass.__init__ should set the array attribute
        """
        expected_array = [10, 3, 8, 2, 8, 17]

        self.assertEqual(self.array_object.array, expected_array)

    def test_eliminate_duplicate(self):
        """
        ArrayClass.eliminate_duplicate should set the array attribute without duplicate elements
        """
        expected_array = [8, 17, 10, 3, 2]

        self.array_object.eliminate_duplicate()

        self.assertEqual(self.array_object.array, expected_array)

    def test_add(self):
        """
        ArrayClass.add should add an element to the array attribute
        """
        element = 6
        expected_array = [10, 3, 8, 2, 8, 17, element]

        self.array_object.add(element)

        self.assertEqual(self.array_object.array, expected_array)

    def test_rank_1(self):
        """
        ArrayClass.rank should return the given element's rank
        """
        element = 8
        expected_index = 3

        index = self.array_object.rank(element)

        self.assertEqual(index, expected_index)

    def test_rank_2(self):
        """
        ArrayClass.rank should return None when the given element is not in the array property
        """
        element = 9

        index = self.array_object.rank(element)

        self.assertIsNone(index)

    def test_order(self):
        """
        ArrayClass.order should sort the array property reverse
        """
        expected_array = [17, 10, 8, 8, 3, 2]

        self.array_object.order()

        self.assertEqual(self.array_object.array, expected_array)

if __name__ == '__main__':
    unittest.main()
