#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import
import unittest

from array_class import ArrayClass


class ArrayClassTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original_value = [10, 3, 8, 2, 8, 17]

    def setUp(self):
        self.array = ArrayClass(self.original_value)

    def test___init__(self):
        """
        ArrayClass.__init__ should set the value attribute
        """
        expected_value = [10, 3, 8, 2, 8, 17]

        self.assertEqual(self.array.value, expected_value)

    def test_eliminate_duplicate(self):
        """
        ArrayClass.eliminate_duplicate should set the value attribute without duplicate elements
        """
        expected_value = [8, 17, 10, 3, 2]

        self.array.eliminate_duplicate()

        self.assertEqual(self.array.value, expected_value)

    def test_add(self):
        """
        ArrayClass.add should add an element to the value attribute
        """
        element = 6
        expected_value = [10, 3, 8, 2, 8, 17, element]

        self.array.add(element)

        self.assertEqual(self.array.value, expected_value)

    def test_rank_1(self):
        """
        ArrayClass.rank should return the given element's rank
        """
        element = 8
        expected_index = 3

        index = self.array.rank(element)

        self.assertEqual(index, expected_index)

    def test_rank_2(self):
        """
        ArrayClass.rank should return None when the given element is not in the array attribute
        """
        element = 9

        index = self.array.rank(element)

        self.assertIsNone(index)

    def test_order(self):
        """
        ArrayClass.order should sort the array attribute reverse
        """
        expected_value = [17, 10, 8, 8, 3, 2]

        self.array.order()

        self.assertEqual(self.array.value, expected_value)

if __name__ == '__main__':
    unittest.main()
