from .symbols import SYM, OP, symtostr, codetostr

sym_code_map = {
    SYM.TYPE:           OP.TAGNAME,
    SYM.HASH:           OP.ID,
    SYM.HASATTRIB:      OP.ATTR_PRESENCE,
    SYM.EQUAL:          OP.ATTR_EXACTLY,
    SYM.INCLUDES:       OP.ATTR_WORD,
    SYM.DASHMATCH:      OP.ATTR_BEGIN,
    SYM.PREFIXMATCH:    OP.ATTR_PREFIX,
    SYM.SUFFIXMATCH:    OP.ATTR_SUFFIX,
    SYM.SUBSTRINGMATCH: OP.ATTR_SUBSTRING,
    SYM.CLASS:          OP.CLASSES,
    SYM.S:              OP.DESCENDANT,
    SYM.GREATER:        OP.CHILDREN,
    SYM.PLUS:           OP.SIBLING_NEXT,
    SYM.TILDE:          OP.SIBLING_SUBSEQUENT,
}


def compile(ast):
    for selector in ast:
        yield (OP.RESET, )

        for combinator, simple_selector in selector:
            yield (sym_code_map[combinator], )

            classes = set()

            for sym, *args in simple_selector:
                if sym == SYM.UNIVERSAL:
                    continue
                elif sym == SYM.CLASS:
                    classes.add(args[0])
                else:
                    yield (sym_code_map[sym], args)

            if classes:
                yield (OP.CLASSES, classes)

        yield (OP.STORE, )
