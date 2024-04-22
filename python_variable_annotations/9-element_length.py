#!/usr/bin/env python3
"""Quack goe the duck type
 _
<(o )___
   (  ._> /
    `---'
      J
     """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck typing an iterable"""
    return [(i, len(i)) for i in lst]
