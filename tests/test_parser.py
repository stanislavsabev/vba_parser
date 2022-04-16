"""Test start module."""

from vba_parser import parser


def test_parser_parse_5():
    """Test start.here."""
    p = parser.Parser()
    actual = p.parse('5')
    expected = {
        "type": "Number",
        "value": 5,
    }
    assert actual == expected
