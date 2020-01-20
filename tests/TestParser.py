from .TestLinePairs import TestLinePairs
from .utils import string_to_ast_repr

__all__ = ("TestParser", )


class TestParser(TestLinePairs):
    def __init__(self, *args, **kwargs):
        super(TestLinePairs, self).__init__(*args, **kwargs)
        self.output_to_repr = string_to_ast_repr

    def testSelector(self):
        self.check_file("parser.selector1.test.gen")
