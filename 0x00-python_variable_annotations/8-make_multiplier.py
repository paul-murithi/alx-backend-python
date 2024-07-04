#!/usr/bin/env python3
"""Complex types - functions
unction make_multiplier that takes a float multiplier as argument and returns
function that multiplies a float by multiplier
"""


from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier"""

    def f(n: float) -> float:
        """Multiplies a float by multiplier """
        return float(n * multiplier)

    return f
