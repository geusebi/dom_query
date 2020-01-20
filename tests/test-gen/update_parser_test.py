from sys import argv
from sys import exit

try:
    from pydom_query import lexer, parse
except ImportError:
    message = ("Couldn't import from pydom_query\n"
               "This script should be run from test-gen directory with "
               "proper PYTHONPATH, i.e.:\n"
               f"$ PYTHONPATH=../.. python {argv[0]} [TESTFILE] ... ")
    raise ImportError(message)

if __name__ == "__main__":
    if len(argv) < 2:
        print(f"Usage:")
        print(f"  PYTHONPATH=../.. python {argv[0]} [TESTFILE] ...")
        exit(1)

    for src_file in argv[1:]:
        gen_file = f"{src_file}.gen"
        src = open(src_file)
        gen = open(gen_file, "w")

        for line in src.read().splitlines():
            if len(line) == 0:
                continue

            try:
                ast = parse(lexer(line))
                result = repr(ast)
            except SyntaxError as e:
                result = repr(e)

            print(line)
            print(result)
            print()

            gen.write(f"{line}\n")
            gen.write(f"{result}\n")
