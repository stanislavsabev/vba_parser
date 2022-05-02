"""VBA Parser to produce an AST tree."""

from typing import Dict, Any

from vba_parser import tokenizer as tk


class Parser:

    def __init__(self) -> None:
        self._tokenizer = tk.Tokenizer()
        self._lookahead: tk.Token = tk.EOF_TOKEN

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

    # program
    #   : literal
    #   ;
    def program(self):
        """Program AST."""
        return dict(
            type='program',
            value=self.literal())

    # literal
    #   : numeric_literal
    #   | string_literal
    #   ;
    def literal(self):
        if self._lookahead.type == 'NUMBER':
            return self.numeric_literal()
        elif self._lookahead.type == 'STRING':
            return self.string_literal()
        else:
            raise SyntaxError('Unexpected literal production.')

    def numeric_literal(self):
        """Numeric literal AST"""
        token = self._consume('NUMBER')
        return dict(
            type='numeric_literal',
            value=int(token.value),
        )

    def string_literal(self):
        """Numeric literal AST"""
        token = self._consume('STRING')
        result = dict(
            type='string_literal',
            value=token.value[1: -1],
        )
        return result

    def _consume(self, token_type: str) -> tk.Token:
        token = self._lookahead
        if token is tk.EOF_TOKEN:
            raise SyntaxError(f'Unexpected end of input, expected: {token_type}')
        if token.type != token_type:
            raise SyntaxError(
                f'Unexpected token type, expected: {token_type}, got {token.type}')

        self._lookahead = self._tokenizer.next_token()
        return token
