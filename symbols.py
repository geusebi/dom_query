from types import SimpleNamespace as NameSpace

__all__ = ["SYM", "SYM_COMBINATORS", "SYM_ATTRIBMATCH", "symtostr"
           "OP", "OP_COMBINATORS", "OP_FILTER", "codetostr", ]

sym_names = (
    "EQUAL", "INCLUDES", "DASHMATCH", "PREFIXMATCH",
    "SUFFIXMATCH", "SUBSTRINGMATCH",
    "UNIVERSAL", "IDENT", "HASH", "CLASS", "STRING",
    "PLUS", "GREATER", "COMMA", "TILDE", "S", "LETTER",
    "HASATTRIB", "ATTRIBOPEN", "ATTRIBCLOSE", "START",
    "END", "TYPE", "LOAD_ELEMS", "YIELD", "CLASSES",
    "DESCENDANT",
)

sym_name_map = dict(enumerate(sym_names))

SYM = NameSpace(**{name: value
                   for value, name
                   in sym_name_map.items()})

SYM_COMBINATORS = (
    SYM.PLUS,
    SYM.GREATER,
    SYM.TILDE,
    SYM.S,
)

SYM_ATTRIBMATCH = (
    SYM.EQUAL,
    SYM.INCLUDES,
    SYM.DASHMATCH,
    SYM.PREFIXMATCH,
    SYM.SUFFIXMATCH,
    SYM.SUBSTRINGMATCH,
)


def symtostr(sym):
    return sym_name_map[sym]


op_names = (
    "TAGNAME", "ID", "ATTR_PRESENCE", "ATTR_EXACTLY", "ATTR_WORD",
    "ATTR_BEGIN", "ATTR_PREFIX", "ATTR_SUFFIX", "ATTR_SUBSTRING",
    "CLASSES", "DESCENDANT", "CHILDREN", "SIBLING_NEXT",
    "SIBLING_SUBSEQUENT", "STORE", "RESET",
)

op_name_map = dict(enumerate(op_names))

OP = NameSpace(**{name: value
                  for value, name
                  in op_name_map.items()})

OP_COMBINATORS = {
    OP.DESCENDANT,
    OP.CHILDREN,
    OP.SIBLING_NEXT,
    OP.SIBLING_SUBSEQUENT,
}

OP_FILTERS = {
    OP.TAGNAME,
    OP.ID,
    OP.ATTR_PRESENCE,
    OP.ATTR_EXACTLY,
    OP.ATTR_WORD,
    OP.ATTR_BEGIN,
    OP.ATTR_PREFIX,
    OP.ATTR_SUFFIX,
    OP.ATTR_SUBSTRING,
    OP.CLASSES,
}


def codetostr(code):
    return op_name_map[code]
