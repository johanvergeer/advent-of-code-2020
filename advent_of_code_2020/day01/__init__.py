import math
from itertools import combinations
from typing import List, Tuple


def _get_combination(
    numbers: List[int], required_length: int, required_sum: int
) -> Tuple[int, ...]:
    for combination in combinations(numbers, required_length):
        if sum(combination) == required_sum:
            return combination

    raise ValueError(
        f"No combination found with {required_length} numbers "
        f"that sum up to {required_sum}."
    )


def get_factor(numbers: List[int], required_length: int, required_sum: int) -> int:
    combination = _get_combination(numbers, required_length, required_sum)
    return math.prod(combination)
