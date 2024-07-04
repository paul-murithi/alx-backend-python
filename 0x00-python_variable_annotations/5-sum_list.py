#!/usr/bin/env python3
"""Complex types - list of floats
function sum_list which takes a list input_list of floats as argument and
returns their sum as a float."""


from typing import Iterator, Callable, Union, Optional, List


def sum_list(input_list: List[float]) -> float:
    """Returns their sum as a float"""
    return sum(input_list)
