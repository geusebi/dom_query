from pydom_query import lexer, parse
from .TestLinePairs import TestLinePairs

__all__ = ("TestParser", )


def to_ast(s):
    return parse(lexer(s))


class TestParser(TestLinePairs):
    def testSelector(self):
        name = "parser.selector1.test.gen"
        self.check_file(name, to_ast)
