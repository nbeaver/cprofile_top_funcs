#! /usr/bin/env python
import pstats
import sys

if __name__ == '__main__':
    for filepath in sys.argv[1:]:
        print(filepath)
        stats = pstats.Stats(filepath)
        stats.sort_stats('time').print_stats(4)
