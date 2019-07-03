#!/usr/bin/env python3
import argparse
import sys


def get_options(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-i", "--input", help="Your input file.")
    parser.add_argument("-o", "--output", help="Your destination output file.")
    parser.add_argument("-n", "--number", help="A number.", type=int)
    parser.add_argument("-v", "--verbose", dest='verbose', action='store_true', help="Verbose mode.")
    options = parser.parse_args(args)
    return options


def main():
    options = get_options(sys.argv[1:])
    if options.verbose:
        print("Verbose mode on")
    else:
        print("Verbose mode off")

    print(options.input)
    print(options.output)
    print(options.number)


if __name__ == '__main__':
    main()

