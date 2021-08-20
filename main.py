#!/usr/bin/env python3

import random
import argparse
import sys

from zalgo import zalgo


def handle_arguments():
    parser = argparse.ArgumentParser(description='Generate zalgo text for '
                                                 'given input.')
    parser.add_argument('-q', '--variations', type=int, default=1,
                        dest='quantity',
                        help='number of text variations to generate')
    parser.add_argument('-a', '--additions', type=int, default=3,
                        dest='adds_per_char',
                        help='number of combining (zalgo) characters to add '
                             ' per letter')
    parser.add_argument('text', nargs='*', default='hello world')
    return parser


def run():
    parser = handle_arguments()
    args = parser.parse_args()
    text = args.text
    if not sys.stdin.isatty():
        text = [x.strip() for x in sys.stdin.readlines()]
    for i in range(args.quantity):
        print(zalgo(' '.join(text), args.adds_per_char))


if __name__ == "__main__":
    run()
