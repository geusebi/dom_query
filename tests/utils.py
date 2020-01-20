from pydom_query.symbols import symtostr
from pydom_query import lexer, parse
import warnings
import html5lib
from xml.dom.minidom import Childless as _Childless

_PARSE_FRAGMENT_KWARGS = {
    "treebuilder": "dom",
    "namespaceHTMLElements": False,
}

_SERIALIZE_KWARGS = {
    "tree": "dom",
    "minimize_boolean_attributes": True,
    "use_trailing_solidus": False,
    "omit_optional_tags": True,
}


def parse_dom(str_or_fh, *args, **kwargs):
    kwargs = {**_PARSE_FRAGMENT_KWARGS, **kwargs}

    # Ignore a html5lib specific warning
    # todo: regularly check whether it is still the case
    #  to ignore it.
    warnings.filterwarnings(
        "ignore",
        "Using or importing the ABCs from 'collections'",
        DeprecationWarning,
        "html5lib.treebuilders.dom",
        4
    )

    tree = html5lib.parse(str_or_fh, *args, **kwargs)
    return tree


def serialize_dom(node, *args, **kwargs):
    kwargs = {**_SERIALIZE_KWARGS, **kwargs}

    return html5lib.serializer.serialize(
        node, *args, **kwargs
    )


def iter_nodes(root):
    if not isinstance(root, _Childless):
        for node in root.childNodes:
            yield node
            yield from iter_nodes(node)


def string_to_tokens_repr(s):
    try:
        tokens = lexer(s)
        parts = []
        for sym, value in tokens:
            if sym is None and value is None:
                parts.append("(SENTINEL)")
            elif value is not None:
                parts.append(f"({symtostr(sym)} {value!r})")
            else:
                parts.append(f"({symtostr(sym)})")
        return " ".join(parts)
    except Exception as e:
        return repr(e)


def string_to_ast_repr(s):
    try:
        ast = parse(lexer(s))
        h_ast = []
        for selector in ast:
            for combinator, simple_selector in selector:
                criteria = []
                for criterion, *args in simple_selector:
                    if args is None:
                        criteria.append(symtostr(criterion))
                    else:
                        criteria.append((symtostr(criterion), *args))
                h_ast.append((symtostr(combinator), tuple(criteria)))
        return repr(tuple(h_ast))
    except Exception as e:
        return repr(e)
