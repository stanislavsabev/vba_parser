"""VBA Parser to produce an AST tree."""


from typing import Dict, Any

from vba_parser import tokenizer


class Parser:

    def __init__(self) -> None:
        self._tokenizer = tokenizer.Tokenizer()

    def parse(self, input_str: str) -> Dict[str, Any]:
        """Parse statements list.

        Args:
            input_str: A list of string statements.

        Returns:
            A dict representing the AST tree.
        """
        value = self._tokenizer.Number(input_str)
        return dict(
            type='Number',
            value=value,
        )
