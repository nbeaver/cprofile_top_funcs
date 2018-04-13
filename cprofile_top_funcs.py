import pstats
import argparse
import os.path

def readable_file(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(
            'not an existing file: {}'.format(path))
    if not os.access(path, os.R_OK):
        raise argparse.ArgumentTypeError(
            'not a readable file: {}'.format(path))
    return path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Get top functions by time.'
    )
    parser.add_argument(
        '-n', '--n_funcs',
        type=int,
        help='Number of functions to print.',
        required=False,
        default=3,
    )
    parser.add_argument(
        'filepaths',
        type=readable_file,
        help='Directory to read from.',
        nargs='+',
    )
    args = parser.parse_args()

    for filepath in args.filepaths:
        stats = pstats.Stats(filepath)
        stats.sort_stats('time').print_stats(args.n_funcs)
