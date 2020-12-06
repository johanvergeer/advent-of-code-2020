from pathlib import Path
from typing import List

import pytest

from advent_of_code_2020.day02 import (
    AmountOfCharactersPasswordPolicy,
    get_valid_passwords,
    parse_password_and_amount_of_characters_password_policy,
    parse_password_and_character_at_position_password_policy,
)


@pytest.fixture
def _passwords_with_policies() -> List[str]:
    with (Path(__file__).parent / "input.txt").open() as passwords_file:
        return passwords_file.readlines()


def test_parse_password_with_policy() -> None:
    assert parse_password_and_amount_of_characters_password_policy(
        "6-9 z: qzzzzxzzfzzzz"
    ) == (
        "qzzzzxzzfzzzz",
        AmountOfCharactersPasswordPolicy("z", 6, 9),
    )


def test_get_valid_passwords__amount_of_characters_password_policy(
    _passwords_with_policies,
) -> None:
    passwords_with_policies = [
        parse_password_and_amount_of_characters_password_policy(pp)
        for pp in _passwords_with_policies
    ]

    assert len(get_valid_passwords(passwords_with_policies)) == 506


def test_get_valid_passwords__character_at_position_password_policy(
    _passwords_with_policies,
) -> None:
    passwords_with_policies = [
        parse_password_and_character_at_position_password_policy(pp)
        for pp in _passwords_with_policies
    ]

    assert len(get_valid_passwords(passwords_with_policies)) == 443
