"""Test start module."""

import pytest

from vba_parser import parser, tokenizer


def test_create():
    p = parser.Parser()
    assert p is not None


def test_numeric_literal(random_positive_int):
    """Test numeric literal."""
    number = random_positive_int
    p = parser.Parser()
    lookahead = tokenizer.Token(type='NUMBER', value=number)
    p._lookahead = lookahead
    actual = p.numeric_literal()
    expected = dict(
        type="NumericLiteral",
        value=number,
    )
    assert actual == expected


@pytest.mark.parametrize(
    'code, program_contents',
    [
        ('5', dict(type='NumericLiteral', value=5)),
        ('"abc"', dict(type='StringLiteral', value='abc')),
        ('"5"', dict(type='StringLiteral', value='5')),
    ]
)
def test_parse_program(code, program_contents):
    """Test program."""
    p = parser.Parser()
    actual = p.parse(code)
    expected = dict(
        type="Program",
        value=program_contents
    )
    assert actual == expected
