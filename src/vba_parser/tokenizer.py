"""A tokenizer to pull and categorize the lexical syntax of a VBA code."""
import re
from typing import Optional
from collections import namedtuple
from vba_parser import spec


class UnknownTokenError(Exception):
    pass


Token = namedtuple('Token', ['type', 'value'], defaults=['', None])


class Tokenizer:
    """A tokenizer class to pull and categorize the
        lexical syntax of a VBA code.

    """

    def __init__(self) -> None:
        """Constructor (not used)."""
        self._string = ''
        self._cursor = 0

    def init(self, string: str) -> None:
        """Init Tokenizer.

        Args:
            string: A string, program input.
        """
        self._string = string
        self._cursor = 0

    def has_more_tokens(self) -> bool:
        """Return `True`, unless the end if input is reached."""
        return self._cursor < len(self._string)

    def next_token(self) -> Optional[Token]:
        """Match next token accorting to the spec.

        Returns:
            A Token, or None, if the end of input is reached.

        Raises:
            UnknownTokenError if no token is matched.
        """
        if not self.has_more_tokens():
            return None
        string = self._string[self._cursor:]

        # Match Number
        match = re.match(spec.Number, string)
        if match:
            return self.number(match.string)

        raise UnknownTokenError(f'Unknown token at {self._cursor}')

    def number(self, string) -> int:
        """Parse a `NUMBER` token."""
        return Token(type='NUMBER', value=int(string))
