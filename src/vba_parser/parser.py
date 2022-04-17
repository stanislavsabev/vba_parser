"""VBA Parser to produce an AST tree."""

from typing import Dict, Any

from vba_parser import tokenizer


class Parser:

    def __init__(self) -> None:
        self._tokenizer = tokenizer.Tokenizer()
        self._lookahead: tokenizer.Token = None

    def parse(self, string: str) -> Dict[str, Any]:
        """Parse statements list.

        Args:
            string: A string with statements to parse.

        Returns:
            A dict, the AST tree.
        """
        self._tokenizer.init(string)
        self._lookahead = self._tokenizer.next_token()
        return self.program()

    def program(self):
        """Program AST."""
        return dict(
            type='Program',
            value=self.numeric_literal())

    def numeric_literal(self):
        """Numeric literal AST"""
        token = self._consume('NUMBER')
        return dict(
            type='NumericLiteral',
            value=token.value,
        )

    def _consume(self, token_type: str) -> tokenizer.Token:
        token = self._lookahead
        if token is None:
            raise SyntaxError(f'Unexpected end of input, expected: {token_type}')
        if token.type != token_type:
            raise SyntaxError(
                f'Unexpected token type, expected: {token_type}, got {token.type}')

        self._lookahead = self._tokenizer.next_token()
        return token
