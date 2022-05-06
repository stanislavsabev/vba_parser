"""Test start module."""

import pytest

from vba_parser import tokenizer


@pytest.fixture
def tokenizer_fixture() -> tokenizer.Tokenizer:
    return tokenizer.Tokenizer()


def test_create():
    """Test start.here."""
    sut = tokenizer.Tokenizer()
    assert sut is not None
    assert sut._string == ''
    assert sut._cursor == 0


def test_init():
    """Test start.here."""
    sut = tokenizer.Tokenizer()
    sut.init('abc')
    assert sut._string == 'abc'
    assert sut.has_more_tokens()


def test_number_token(tokenizer_fixture, random_positive_int):
    """Test the number Token production."""
    expected = tokenizer.Token(type='NUMBER', value=str(random_positive_int))
    tokenizer_fixture.init(str(random_positive_int))
    actual = tokenizer_fixture.next_token()
    assert actual == expected


@pytest.mark.parametrize('token', [
    '"hello ""world""!"',
    '"hello world!"',
    '"\'"',
    '""""',
    '"""a""""sd"""""',
    '"asdf"',
    '"ABC"',
    pytest.param('"ABC" ', marks=pytest.mark.xfail(raises=AssertionError)),
    pytest.param(' "ABC"', marks=pytest.mark.xfail(raises=tokenizer.UnknownTokenError)),
])
def test_string_token(tokenizer_fixture, token):
    """Test the string Token production."""
    expected = tokenizer.Token(type='STRING', value=token)
    tokenizer_fixture.init(token)
    actual = tokenizer_fixture.next_token()
    assert actual == expected


@pytest.mark.parametrize('token', [
    "'hello world",
    "' hello world  ",
    "'    12345_!@><?\"''''  ",
    pytest.param(" '", marks=pytest.mark.xfail(raises=AssertionError)),
    pytest.param("3'", marks=pytest.mark.xfail(raises=AssertionError)),
    pytest.param("A'", marks=pytest.mark.xfail(raises=tokenizer.UnknownTokenError)),
])
def test_comment_token(tokenizer_fixture, token):
    """Test the comment Token production."""
    expected = tokenizer.EOF_TOKEN
    tokenizer_fixture.init(token)
    actual = tokenizer_fixture.next_token()
    assert actual == expected


@pytest.mark.parametrize('token', [
    " ",
    " " * 10,
    "\t",
    "\r\n\t\f\v ",
    pytest.param("'", marks=pytest.mark.xfail(raises=AssertionError)),
    pytest.param("3", marks=pytest.mark.xfail(raises=AssertionError)),
    pytest.param("A", marks=pytest.mark.xfail(raises=tokenizer.UnknownTokenError)),
])
def test_witespace_token(tokenizer_fixture, token):
    """Test the witespace Token production."""
    expected = tokenizer.Token(type='WHITESPACE', value=token)
    tokenizer_fixture.init(token)
    actual = tokenizer_fixture.next_token()
    assert actual == expected
