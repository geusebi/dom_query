from xml.dom.minidom import Childless, Element
from .symbols import OP

api = {}


def implement(opcode):
    def api_set(impl):
        api[opcode] = impl
    return api_set


@implement(OP.TAGNAME)
def tag_equal(name):
    def f(elem):
        return elem.tagName == name
    return f


@implement(OP.ID)
def id_equal(name):
    def f(elem):
        return (elem.hasAttribute("id") and
                elem.getAttribute("id") == name)
    return f


@implement(OP.ATTR_PRESENCE)
def has_attribute(name):
    def f(elem):
        return elem.hasAttribute(name)
    return f


@implement(OP.ATTR_EXACTLY)
def attribute_equal(name, string):
    def f(elem):
        return (elem.hasAttribute(name) and
                elem.getAttribute(name) == string)
    return f


@implement(OP.ATTR_WORD)
def attribute_word(name, word):
    def f(elem):
        return (elem.hasAttribute(name) and
                word in elem.getAttribute(name).split())
    return f


@implement(OP.ATTR_PREFIX)
def attribute_starts(name, string):
    def f(elem):
        return (elem.hasAttribute(name) and
                elem.getAttribute(name).startswith(string))
    return f


@implement(OP.ATTR_BEGIN)
def attribute_begins(name, string):
    def f(elem):
        if not elem.hasAttribute(name):
            return False
        value = elem.getAttribute(name)
        return (value.startswith(string) or
                value.startswith(f"{string}-"))
    return f


@implement(OP.ATTR_SUFFIX)
def attribute_ends(name, string):
    def f(elem):
        return (elem.hasAttribute(name) and
                elem.getAttribute(name).endswith(string))
    return f


@implement(OP.ATTR_SUBSTRING)
def attribute_contains(name, string):
    def f(elem):
        return (elem.hasAttribute(name) and
                string in elem.getAttribute(name))
    return f


@implement(OP.CLASSES)
def has_classes(classes):
    def f(elem):
        return (elem.hasAttribute("class") and
                classes.issubset(elem.getAttribute("class").split()))
    return f


@implement(OP.DESCENDANT)
def combinator_descendant(nodes):
    for node in nodes:
        yield from recurse_descendant(node.childNodes)


def recurse_descendant(nodes):
    for node in nodes:
        if isinstance(node, Childless):
            continue
        if isinstance(node, Element):
            yield node
        yield from recurse_descendant(node.childNodes)


@implement(OP.CHILDREN)
def combinator_children(nodes):
    for node in nodes:
        if isinstance(node, Childless):
            continue
        for elem in node.childNodes:
            if isinstance(elem, Element):
                yield elem


@implement(OP.SIBLING_NEXT)
def combinator_adjacent(nodes):
    for node in nodes:
        sibling = node.nextSibling
        while sibling is not None and not isinstance(sibling, Element):
            sibling = sibling.nextSibling
        if sibling is not None:
            yield sibling


@implement(OP.SIBLING_SUBSEQUENT)
def combinator_sibling(nodes):
    # Document type (no parent) is not handled since it should
    # happen only in descendants combinator
    for node in nodes:
        for elem in node.parent.childNodes:
            # todo: this should return subsequent siblings only
            if isinstance(elem, Element) and not node.isSameNode(elem):
                yield elem
