"""Example for how to use the `vba_parser` package."""

import json
from vba_parser import parser


def main():
    """Entry point for this script."""
    ast = json.dumps(parser.Parser().parse('5'), indent=4)
    print(ast)


if __name__ == '__main__':
    main()
