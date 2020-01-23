from .compiler import compile
from .vm import execute
from .minidom_api import api as api

__all__ = ["select_iter", "select", "select_all", ]


def select_iter(node, query):
    """Generator which yield elements matched by `query`."""
    code = compile(query)
    return execute(node, code, api)


def select(node, query):
    """Return the first element matched by `query`."""
    try:
        return next(select_iter(node, query))
    except StopIteration:
        return None


def select_all(node, query):
    """Return every element matched by `query`."""
    return tuple(select_iter(node, query))
