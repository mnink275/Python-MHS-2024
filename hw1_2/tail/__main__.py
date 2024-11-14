import click
import sys

from collections import deque

def from_stdin():
    last_lines = deque(maxlen=17)
    for line in sys.stdin:
        if not line:
            break

        last_lines.append(line)

    for line in last_lines:
        print(line, end='')

def from_files(filenames: tuple):
    for idx, filename in enumerate(filenames):
        last_lines = deque(maxlen=10)
        with open(filename, 'r') as file:
            for line in file:
                last_lines.append(line)
        if len(filenames) > 1:
            print(f'==> {filename} <==')
        for line in last_lines:
            print(line, end='')
        
        if idx < len(filenames) - 1:
            print()

@click.command()
@click.argument('filenames', metavar='[FILE]...', required=False, default=None, nargs=-1)
def tail(filenames: tuple):
    """
    Simple tail-like program.
    Print the last 10 lines of each FILE to standard output.
    With more than one FILE, precede each with a header giving the file name.

    With no FILE, or when FILE is -, read standard input and print the last 17 lines.
    """

    if filenames:
        from_files(filenames)
    else:
        from_stdin()

if __name__ == '__main__':
    tail()
