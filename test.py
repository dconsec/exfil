#!/usr/bin/env python3

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Print a personalized hello message"
    )
    parser.add_argument(
        "-n", "--name",
        default="world",
        help="Name to greet (default: world)"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print("Hello, {}!".format(args.name))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(1)
