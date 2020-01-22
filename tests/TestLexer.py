from pydom_query import lexer
from .TestLinePairs import TestLinePairs

__all__ = ("TestLexer", )


def to_tokens(s):
    return tuple(lexer(s))


class TestLexer(TestLinePairs):
    def testSingleSelectors(self):
        name = "selector.lexer.test-gen"
        self.check_file(name, to_tokens)

    def testAllTokens(self):
        name = "all_tokens.lexer.test-gen"
        self.check_file(name, to_tokens)
