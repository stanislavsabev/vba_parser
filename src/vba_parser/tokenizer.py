"""A tokenizer to pull and categorize the lexical syntax of a VBA code."""


class Tokenizer:
    """A tokenizer class to pull and categorize the
        lexical syntax of a VBA code.

    """

    def __init__(self, code: str) -> None:
        """Init tokenizer."""
        self._code = code
        self._cursor_position = 0
