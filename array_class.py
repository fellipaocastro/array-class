# coding: utf-8


class ArrayClass(object):
    def __init__(self, array):
        self.array = list(array)

    def eliminate_duplicate(self):
        self.array = list(set(self.array))

    def add(self, element):
        self.array.append(element)

    def rank(self, element):
        if element in self.array:
            return self.array.index(element) + 1

    def order(self):
        self.array = sorted(self.array, reverse=True)
