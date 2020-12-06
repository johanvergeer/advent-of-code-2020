from pathlib import Path
from typing import List

import pytest

from advent_of_code_2020.day01 import get_factor


@pytest.fixture(scope="session")
def _numbers() -> List[int]:
    with (Path(".") / "input.txt").open() as numbers_file:
        return [int(num.strip()) for num in numbers_file.readlines()]


@pytest.mark.parametrize(
    "required_length,expected_factor", [(2, 471019), (3, 103927824)]
)
def test_get_factor(_numbers, required_length, expected_factor) -> None:
    assert get_factor(_numbers, required_length, 2020) == expected_factor


def test_get_factor__no_combination_found():
    with pytest.raises(ValueError) as err:
        get_factor([1, 2, 3], 2, 2020)

    assert str(err.value) == "No combination found with 2 numbers that sum up to 2020."
