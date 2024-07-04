#!/usr/bin/env python3
"""Let's duck type an iterable object"""

from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate function’s parameters and return values with
    the appropriate types"""

    return [(i, len(i)) for i in lst]
