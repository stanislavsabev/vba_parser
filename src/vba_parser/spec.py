"""A Spec for the VBA language."""


SPEC = [
    ('INTEGER', r'^\d+'),
    ('STRING', r'^\"(?:\"\"|[^\"])*\"'),
    ('WHITESPACE', r'^\s+'),
    ('COMMENT', r'^\'.*$'),
]
