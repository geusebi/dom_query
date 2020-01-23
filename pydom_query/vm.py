from .symbols import OP

__all__ = ["execute", ]


def execute(root, code, api):
    output = {}

    elements = None
    for opcode, *args in code:
        if opcode in OP.filters:
            elements = filter(api[opcode](*args[0]), elements)

        elif opcode in OP.combinators:
            elements = api[opcode](elements)

        elif opcode == OP.STORE:
            for element in elements:
                if element not in output:
                    yield element

        elif opcode == OP.RESET:
            elements = [root]

        else:
            raise NotImplemented
