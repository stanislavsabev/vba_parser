"""Pytest fixtures."""

import random
import string


def random_positive_int() -> int:
    """Random positive int (up to 100'000'000)"""
    return random.randint(0, 100_000_000)


def random_vba_string() -> str:
    """Create random vba string (up to 255 chars)"""
    s = ''.join(random.choice(string.ascii_letters)
                for _ in range(random.randint(0, 256)))
    return f'"{s}"'
