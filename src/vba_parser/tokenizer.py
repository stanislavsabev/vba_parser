"""A tokenizer to pull and categorize the lexical syntax of a VBA code."""
import re

from vba_parser import spec


class UnknownTokenError(Exception):
    pass


class Tokenizer:
    """A tokenizer class to pull and categorize the
        lexical syntax of a VBA code.

    """

    def __init__(self) -> None:
        """Init tokenizer."""
        self._code = ''
        self._cursor_position = 0

    def Number(self, statement: str) -> int:
        """Parses Number token.

        Args:
            statement: A string to match.
        """
        m = re.match(spec.Number, statement)
        if m is None:
            raise UnknownTokenError
        return int(m.string)
