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


def test_init(tokenizer_fixture):
    """Test start.here."""
    sut = tokenizer.Tokenizer()
    sut.init('abc')
    assert sut._string == 'abc'
    assert sut.has_more_tokens()

def test_number_token(tokenizer_fixture, random_positive_int):
    """Test the number Token production."""
    
    expected = tokenizer.Token(type='NUMBER', value=random_positive_int)
    actual = tokenizer_fixture.number_token(str(random_positive_int))
    assert actual == expected


@pytest.mark.parametrize('vba_string', [
    '"hello ""world""!"',
    '"hello world!"',
    '"\'"',
    '""""',
    '"""a""""sd"""""',
    '"asdf"',
])
def test_number_token(tokenizer_fixture, vba_string):
    """Test the string Token production."""
    
    expected = tokenizer.Token(type='STRING', value=vba_string)
    actual = tokenizer_fixture.string_token(str(vba_string))
    assert actual == expected


