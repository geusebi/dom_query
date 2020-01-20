__all__ = ["SYM", "SYM_COMBINATORS", "SYM_ATTRIBMATCH",
           "OP", "OP_COMBINATORS", "OP_FILTERS", ]


class NamedInt(int):
    def __new__(cls, name, value):
        o = super().__new__(cls, value)
        o.name = name
        return o

    def __repr__(self):
        return self.name


class MirrorNameSpace(object):
    def __setattr__(self, name, value):
        sym = NamedInt(name, value)
        self.__dict__[name] = sym
        self.__dict__[value] = sym


SYM = MirrorNameSpace()


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


OP = MirrorNameSpace()

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
