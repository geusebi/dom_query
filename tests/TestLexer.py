import unittest
from os import path
from itertools import count
from pydom_query import lexer
from .utils import stringify_tokens

__all__ = ("TestLexer", )


class TestLexer(unittest.TestCase):
    def testSingleSelectors(self):
        self.check_test_gen("lexer.simple_selector.test.gen")

    def testAllTokens(self):
        self.check_test_gen("lexer.all_tokens.test.gen")

    def check_test_gen(self, name):
        root = path.join(path.dirname(__file__), "test-gen")
        filepath = path.join(root, name)

        fh = open(filepath)
        lines = iter(fh.read().splitlines())

        for i, string, expect in zip(count(), lines, lines):
            with self.subTest(text=string):
                output = stringify_tokens(lexer(string))
                self.assertEqual(output, expect)

        fh.close()
