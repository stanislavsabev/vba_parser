"""Example for how to use the `vba_parser` package."""

from vba_parser import parser


def main():
    """Entry point for this script."""
    print(parser.Parser().parse('5'))


if __name__ == '__main__':
    main()
