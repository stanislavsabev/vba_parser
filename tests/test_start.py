"""Test start module."""

from vba_parser import start


def test_start_here():
    """Test start.here."""
    expected = 'Your code goes here!'
    actual = start.here()
    assert actual == expected
