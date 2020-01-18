from types import SimpleNamespace as NameSpace

__all__ = ["SYM", "SYM_COMBINATORS", "SYM_ATTRIBMATCH", "symtostr",
           "OP", "OP_COMBINATORS", "OP_FILTERS", "codetostr", ]

SYM = NameSpace()

(SYM.ATTRIBOPEN,     SYM.COMMA,
 SYM.ATTRIBCLOSE,    SYM.UNIVERSAL,
 SYM.EQUAL,          SYM.IDENT,
 SYM.INCLUDES,       SYM.HASH,
 SYM.DASHMATCH,      SYM.CLASS,
 SYM.PREFIXMATCH,    SYM.STRING,
 SYM.SUFFIXMATCH,    SYM.LETTER,
 SYM.SUBSTRINGMATCH, SYM.START,
 SYM.S,              SYM.END,
 SYM.PLUS,           SYM.HASATTRIB,
 SYM.GREATER,        SYM.TYPE,
 SYM.TILDE,          SYM.DESCENDANT,
 ) = range(24)

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

sym_name_map = {sym: name
                for name, sym
                in SYM.__dict__.items()}


def symtostr(sym):
    return sym_name_map[sym]


OP = NameSpace()

(OP.TAGNAME,            OP.ATTR_PRESENCE,
 OP.ID,                 OP.ATTR_EXACTLY,
 OP.DESCENDANT,         OP.ATTR_WORD,
 OP.CHILDREN,           OP.ATTR_BEGIN,
 OP.SIBLING_NEXT,       OP.ATTR_PREFIX,
 OP.SIBLING_SUBSEQUENT, OP.ATTR_SUFFIX,
 OP.STORE,              OP.ATTR_SUBSTRING,
 OP.RESET,              OP.CLASSES,
 ) = range(16)

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

op_name_map = {sym: name
               for name, sym
               in OP.__dict__.items()}


def codetostr(code):
    return op_name_map[code]
