"""Test start module."""

from unittest.mock import MagicMock
import mock
import pytest

from vba_parser import parser
from vba_parser import tokenizer as tk


@pytest.fixture
def parser_fixture() -> parser.Parser:
    return parser.Parser()


def test_create():
    p = parser.Parser()
    assert p is not None


@pytest.mark.parametrize(
    'code, program_value',
    [
        ('5', dict(type='numeric_literal', value=5)),
        ('"abc"', dict(type='string_literal', value='"abc"')),
        ('"5"', dict(type='string_literal', value='"5"')),
    ]
)
def test_parse(parser_fixture, code, program_value):
    """Test program."""
    actual = parser_fixture.parse(code)
    expected = dict(
        type="program",
        value=program_value
    )
    assert actual == expected


def test_numeric_literal(parser_fixture, random_positive_int):
    """Test numeric literal."""
    p = parser_fixture
    number = random_positive_int
    p._lookahead = tk.Token(type='NUMBER', value=number)
    actual = p.numeric_literal()
    expected = dict(
        type="numeric_literal",
        value=number,
    )
    assert actual == expected


@pytest.mark.parametrize('string', [
    '"hello ""world""!"',
    '"hello world!"',
    '"\'"',
    '""""',
    '"""a""""sd"""""',
    '"asdf"',
    pytest.param('asdf', marks=pytest.mark.xfail),
    pytest.param('""asdf"', marks=pytest.mark.xfail),
    pytest.param('"asdf""', marks=pytest.mark.xfail),
    pytest.param('""""asdf""', marks=pytest.mark.xfail),
    pytest.param('"""asdf"""', marks=pytest.mark.xfail),
])
def test_string_literal(parser_fixture, string):
    p = parser_fixture
    p._lookahead = tk.Token(type='STRING', value=string)
    actual = p.string_literal()
    expected = dict(
        type="string_literal",
        value=string,
    )
    assert actual == expected


@pytest.mark.parametrize('token_type, token_value', [
    ('NUMBER', 5),
    ('STRING', '"ABC"'),
    ('STRING', '"5"'),
])
def test_consume_calls_next_token(parser_fixture, token_type, token_value):
    """Parser consume to call next token after it consumes valid token."""
    p = parser_fixture
    lookahead_mock = MagicMock()
    lookahead_mock.type = token_type
    lookahead_mock.value = token_value
    p._lookahead = lookahead_mock
    tokenizer_mock = MagicMock()
    p._tokenizer = tokenizer_mock

    p._consume(token_type)
    tokenizer_mock.next_token.assert_called_once()


@mock.patch.object(tk.Tokenizer, 'next_token')
def test_consume_raises_on_eof_token(next_token_mock, parser_fixture):
    p = parser_fixture
    p._lookahead = tk.EOF_TOKEN
    with pytest.raises(SyntaxError, match=r'Unexpected end of input'):
        p._consume('STRING')
    next_token_mock.assert_not_called()
