import unittest
from os import path
from itertools import count


class TestLinePairs(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLinePairs, self).__init__(*args, **kwargs)
        self.output_to_repr = lambda x: x

    def check_file(self, name):
        root = path.join(path.dirname(__file__), "test-gen")
        filepath = path.join(root, name)

        fh = open(filepath)
        lines = iter(fh.read().splitlines())

        for i, string, expect in zip(count(0, 2), lines, lines):
            with self.subTest(text=string, lines=(i, i+1)):
                result = self.output_to_repr(string)
                self.assertEqual(result, expect)

        fh.close()
