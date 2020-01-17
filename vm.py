from .symbols import OP, OP_FILTERS, OP_COMBINATORS, codetostr

__all__ = ["execute", ]


def execute(root, code, api):
    output = set()

    elements = None
    for opcode, *args in code:
        if opcode in OP_FILTERS:
            elements = filter(api[opcode](*args[0]), elements)

        elif opcode in OP_COMBINATORS:
            elements = api[opcode](elements)

        elif opcode == OP.STORE:
            for element in elements:
                output.add(element)

        elif opcode == OP.RESET:
            elements = [root]

        else:
            raise NotImplemented

    return tuple(output)
