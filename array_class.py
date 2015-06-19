# coding: utf-8


class ArrayClass(object):
    def __init__(self, value):
        self.value = list(value)

    def eliminate_duplicate(self):
        self.value = list(set(self.value))

    def add(self, element):
        self.value.append(element)

    def rank(self, element):
        self.order()

        if element in self.value:
            return self.value.index(element) + 1

    def order(self):
        self.value = sorted(self.value, reverse=True)
