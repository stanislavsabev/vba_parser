"""Test start module."""

from vba_parser import tokenizer as t


def test_create():
    """Test start.here."""
    tokenizer = t.Tokenizer()
    assert tokenizer is not None
    assert tokenizer._code == ''
    assert tokenizer._cursor_position == 0
