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


def test_number(tokenizer_fixture, random_positive_int):
    """Test the number Token production."""
    tokenizer_fixture.number(str(random_positive_int))
