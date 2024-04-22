#!/usr/bin/env python3
"""suma mixed list and returns a float annotation"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns a float"""
    return sum(mxd_lst)
