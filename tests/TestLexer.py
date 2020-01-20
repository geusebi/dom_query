from pydom_query import lexer
from .TestLinePairs import TestLinePairs

__all__ = ("TestLexer", )


def to_tokens(s):
    return tuple(lexer(s))


class TestLexer(TestLinePairs):
    def testSingleSelectors(self):
        name = "lexer.simple_selector.test.gen"
        self.check_file(name, to_tokens)

    def testAllTokens(self):
        name = "lexer.all_tokens.test.gen"
        self.check_file(name, to_tokens)
