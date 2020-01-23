import unittest
from os import path
from itertools import count


class TestLinePairs(unittest.TestCase):
    def check_file(self, name, func):
        root = path.join(path.dirname(__file__), "test-gen")
        filepath = path.join(root, name)

        fh = open(filepath)
        lines = iter(fh.read().splitlines())

        for i, string, expect in zip(count(0, 2), lines, lines):
            with self.subTest(text=string, lines=(i, i+1)):

                try:
                    result = repr(func(string))
                except Exception as e:
                    result = repr(e)

                self.assertEqual(result, expect)

        fh.close()
