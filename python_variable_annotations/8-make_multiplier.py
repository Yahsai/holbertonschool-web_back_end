#!/usr/bin/env python3
"""That takes a float multiplier as
argument and returns a function that
multiplies a float by multipl"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """REturns a function that multiplies
    the multipliyes by a float"""

    def mult(n: float) -> float:
        return n * multiplier

    return mult
