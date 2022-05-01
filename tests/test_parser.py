"""Test start module."""

import pytest

from vba_parser import parser
from vba_parser import tokenizer
from vba_parser.tokenizer import Token


@pytest.fixture
def parser_fixture():
    return parser.Parser()


def test_create():
    p = parser.Parser()
    assert p is not None


@pytest.mark.parametrize(
    'code, token',
    [
        ('5', dict(type='numeric_literal', value=5)),
        ('"abc"', dict(type='string_literal', value='"abc"')),
        ('"5"', dict(type='string_literal', value='"5"')),
    ]
)
def test_parse_program(code, token):
    """Test program."""
    p = parser.Parser()
    actual = p.parse(code)
    expected = dict(
        type="Program",
        value=token
    )
    assert actual == expected


def test_numeric_literal(random_positive_int):
    """Test numeric literal."""
    number = random_positive_int
    p = parser.Parser()
    p._lookahead = tokenizer.Token(type='NUMBER', value=number)
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
def test_string_literal(string):
    p = parser.Parser()
    p._lookahead = tokenizer.Token(type='STRING', value=string)
    actual = p.string_literal()
    expected = dict(
        type="string_literal",
        value=string,
    )
    assert actual == expected