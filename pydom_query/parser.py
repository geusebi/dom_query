from .symbols import SYM

__all__ = ["parse", ]


def parse(tokens):
    sym = value = None

    # Token control functions
    def advance():
        nonlocal sym, value
        sym, value = next(tokens)

    def accept(kind):
        if sym == kind:
            advance()
            return True
        return False

    def expect(kind):
        if sym == kind:
            advance()
            return True
        raise SyntaxError(
            f"Expected token type ({kind}={kind:d})"
        )

    # Generation rules
    def selector_group():
        group = list()

        group.append(selector())
        while accept(SYM.COMMA):
            group.append(selector())

        return tuple(group)

    def selector():
        sequence = list()
        sequence.append((SYM.S, simple_selector()))
        while sym in SYM.combinators:
            combinator = sym
            advance()
            sequence.append((combinator, simple_selector()))

        return tuple(sequence)

    def simple_selector():
        if sym not in (SYM.UNIVERSAL, SYM.IDENT,
                       SYM.HASH, SYM.CLASS, SYM.ATTRIBOPEN):
            raise SyntaxError("Expected a simple selector")

        criteria = []
        if sym == SYM.UNIVERSAL:
            criteria.append((SYM.UNIVERSAL, ))
            advance()
        elif sym == SYM.IDENT:
            criteria.append((SYM.TYPE, value, ))
            advance()

        while sym in (SYM.HASH, SYM.CLASS, SYM.ATTRIBOPEN):
            if sym == SYM.HASH or sym == SYM.CLASS:
                criteria.append((sym, value, ))
                advance()
            elif sym == SYM.ATTRIBOPEN:
                criteria.append(attrib())

        return tuple(criteria)

    def attrib():
        op = string = None

        expect(SYM.ATTRIBOPEN)

        accept(SYM.S)
        name = value
        expect(SYM.IDENT)
        accept(SYM.S)

        if sym in SYM.attribmatch:
            op = sym
            advance()
            accept(SYM.S)
            if sym == SYM.IDENT or sym == SYM.STRING:
                string = value
                advance()
            else:
                raise SyntaxError("String expected")
            accept(SYM.S)

        expect(SYM.ATTRIBCLOSE)

        if op is not None:
            return op, name, string,
        else:
            return SYM.HASATTRIB, name,

    # Run the parser
    advance()
    expect(SYM.START)
    ast = selector_group()
    expect(SYM.END)

    return ast
