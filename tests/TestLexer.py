from .TestLinePairs import TestLinePairs
from .utils import string_to_tokens_repr

__all__ = ("TestLexer", )


class TestLexer(TestLinePairs):
    def __init__(self, *args, **kwargs):
        super(TestLinePairs, self).__init__(*args, **kwargs)
        self.output_to_repr = string_to_tokens_repr

    def testSingleSelectors(self):
        self.check_file("lexer.simple_selector.test.gen")

    def testAllTokens(self):
        self.check_file("lexer.all_tokens.test.gen")
