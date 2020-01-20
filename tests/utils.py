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
