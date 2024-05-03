#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple with the start and end indexes"""
    return ((page - 1) * page_size, page * page_size)
