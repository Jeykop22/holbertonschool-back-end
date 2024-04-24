#!/usr/bin/env python3
"""
Write a type-annotated function sum_list which takes
a list input_list of floats as arguments
and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum of list of float in argument
    """
    sum: float = 0
    for floats in input_list:
        sum += floats
    return sum
