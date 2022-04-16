"""VBA Parser to produce an AST tree."""


from typing import Dict, Any
import re

from vba_parser import spec


class Parser:

    def parse(self, input_str: str) -> Dict[str, Any]:
        """Parse statements list.

        Args:
            input_str: A list of string statements.

        Returns:
            A dict representing the AST tree.
        """

        value = re.match(spec.Number, input_str)
        return dict(
            type='Number',
            value=int(value.string),
        )
