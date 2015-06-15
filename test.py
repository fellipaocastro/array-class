#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import
import unittest

from array_class import ArrayClass


class ArrayClassTestCase(unittest.TestCase):
    def setUp(self):
        self.original_array = [10, 3, 8, 2, 8, 17]

    def test___init__(self):
        """
        ArrayClass.__init__ should set the array attribute
        """
        array_object = ArrayClass(self.original_array)
        expected_array = [10, 3, 8, 2, 8, 17]

        self.assertEqual(array_object.array, expected_array)

    def test_eliminate_duplicate(self):
        """
        ArrayClass.eliminate_duplicate should set the array attribute without duplicate elements
        """
        array_object = ArrayClass(self.original_array)
        expected_array = [8, 17, 10, 3, 2]

        array_object.eliminate_duplicate()    

        self.assertEqual(array_object.array, expected_array)

    def test_add(self):
        """
        ArrayClass.add should add an element to the array attribute
        """
        array_object = ArrayClass(self.original_array)
        element = 6
        expected_array = [10, 3, 8, 2, 8, 17, element]

        array_object.add(element)    

        self.assertEqual(array_object.array, expected_array)

    def test_rank_1(self):
        """
        ArrayClass.rank should return the given element's rank
        """
        array_object = ArrayClass(self.original_array)
        element = 8
        expected_index = 3

        index = array_object.rank(element)

        self.assertEqual(index, expected_index)

    def test_rank_2(self):
        """
        ArrayClass.rank should return None when the given element is not in the array property
        """
        array_object = ArrayClass(self.original_array)
        element = 8
        expected_index = 3

        index = array_object.rank(element)

        self.assertEqual(index, expected_index)

    def test_order(self):
        """
        ArrayClass.order should sort the array property reverse
        """
        array_object = ArrayClass(self.original_array)
        expected_array = [17, 10, 8, 8, 3, 2]

        array_object.order()

        self.assertEqual(array_object.array, expected_array)


if __name__ == '__main__':
    unittest.main()
