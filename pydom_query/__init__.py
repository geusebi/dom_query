from .lexer import lexer
from .parser import parse
from .compiler import compile
from .vm import execute
from .minidom_api import api as minidom_api

__all__ = ["lexer", "parse", "compile", "execute",
           "minidom_api", "query", ]


def query(node, query):
    #  todo: create other query functions for single and generators
    #    and move code outside of `__init__`
    code = compile(query)
    return execute(node, code, minidom_api)
