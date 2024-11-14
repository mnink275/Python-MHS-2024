import click
import sys

def from_stdin():
    line_counter = 0
    for line in sys.stdin:
        if not line:
            break

        line_counter += 1
        print(f'{line_counter:>6}  {line}', end='')

def from_files(filenames: list):
    line_counter = 0
    for filename in filenames:
        with open(filename, 'r') as file:
            for line in file:
                line_counter += 1
                print(f'{line_counter:>6}  {line}', end='')

@click.command()
@click.argument('filenames', metavar='[FILE]...', required=False, default=None, nargs=-1)
def nl(filenames):
    """
    Simple nl-like program. Works like `nl -b a`.
    Write each FILE to standard output, with line numbers added.

    With no FILE, or when FILE is -, read standard input.
    """

    if filenames:
        from_files(filenames)
    else:
        from_stdin()

if __name__ == '__main__':
    nl()

# echo -e "line 1\n\nline 2" | python3 nl -b a
# 
