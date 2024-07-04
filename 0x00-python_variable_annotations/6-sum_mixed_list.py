#!/usr/bin/env python3
""" Complex types - mixed list
function sum_mixed_list which takes a list mxd_lst of integers and floats and
returns their sum as a float.
"""


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of mixed int and float as float"""
    return float(sum(mxd_lst))
