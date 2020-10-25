import sys


class Buffer:
    def __init__(self, filename: str):
        self.input_file = open(filename, 'r')
        self.all_lines = self.input_file.readlines()

    def trim(self, ncolumns: int):
        for line in self.all_lines:
            if line == '\n' or line == '\t':
                print(line, end='')
            elif len(line) < ncolumns:
                print(line)
            elif len(line) > ncolumns:
                nCharsInline = 0
                for word in line.split(' '):
                    if (nCharsInline + len(word) > ncolumns):
                        if len(word) > ncolumns:
                            print(word, end='')
                        print('\n', end='')
                        nCharsInline = 0
                        pass
                    print(word, end=' ')
                    nCharsInline += len(word) + 1
            pass


def Main(args: list):
    if len(args) < 3:
        print('Missing parameters.')
        print(f'Use: python {args[0]} <maxcolumns> <path/to/file>')
        exit(0)
    try:
        ncol = int(args[1])
    except TypeError:
        print(f'Not possible to convert "{args[1]}" to integer')
        exit(1)

    buff = Buffer(args[2])
    buff.trim(ncol)


if __name__ == '__main__':
    Main(sys.argv)
