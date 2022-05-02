"""A tokenizer to pull and categorize the lexical syntax of a VBA code."""
import re
from collections import namedtuple
from typing import Optional
from vba_parser import spec


class UnknownTokenError(Exception):
    pass


Token = namedtuple('Token', ['type', 'value'], defaults=['', None])
EOF_TOKEN = Token(type='EOF', value=None)


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

    def next_token(self) -> Token:
        """Match next token accorting to the spec.

        Returns:
            A Token, or None, if the end of input is reached.

        Raises:
            UnknownTokenError if none of the supported tokens is matched.
        """
        if not self.has_more_tokens():
            return EOF_TOKEN

        for token_type, regex in spec.SPEC:
            token = self._match(token_type, regex)
            if token is None:
                continue
            return token
        raise UnknownTokenError(f'Unknown token at position {self._cursor}')

    def _match(self, token_type, regex) -> Optional[Token]:
        # Match Number
        string = self._string[self._cursor:]
        match = re.match(regex, string)
        if match:
            self._cursor += len(match.group(0))
            return Token(type=token_type, value=match.group(0))
        else:
            return None
