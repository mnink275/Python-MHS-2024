import click
import sys

def count_stats(lines: list):
    lines_count = len(lines)

    words_count = sum(len(line.split()) for line in lines)
    bytes_count = sum(len(line.encode()) for line in lines)
    return lines_count, words_count, bytes_count

def from_stdin():
    lines = []
    for line in sys.stdin:
        if not line:
            break
        lines.append(line)

    lines_count, words_count, bytes_count = count_stats(lines)
    print(f'{lines_count:>7} {words_count:>7} {bytes_count:>7}')

def from_files(filenames: tuple):
    total_lines_count, total_words_count, total_bytes_count = 0, 0, 0
    for filename in filenames:
        lines = []
        with open(filename, 'r') as file:
            for line in file:
                lines.append(line)

        lines_count, words_count, bytes_count = count_stats(lines)
        total_lines_count += lines_count
        total_words_count += words_count
        total_bytes_count += bytes_count
        print(f'{lines_count:>3} {words_count:>3} {bytes_count:>3} {filename}')

    if len(filenames) > 1:
        print(f'{total_lines_count:>3} {total_words_count:>3} {total_bytes_count:>3} total')

@click.command()
@click.argument('filenames', metavar='[FILE]...', required=False, default=None, nargs=-1)
def wc(filenames: tuple):
    """
    Simple wc-like program.
    Print newline, word, and byte counts for each FILE, and a total line if
    more than one FILE is specified. A word is a non-zero-length sequence of
    printable characters delimited by white space.

    With no FILE, or when FILE is -, read standard input.
    """

    if filenames:
        from_files(filenames)
    else:
        from_stdin()

if __name__ == '__main__':
    wc()
