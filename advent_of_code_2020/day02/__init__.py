from abc import abstractmethod
from typing import List, Protocol, Tuple


class PasswordPolicy(Protocol):
    @abstractmethod
    def validate(self, password: str) -> bool:
        """returns True when the password matches the policy, else False"""
        ...


class AmountOfCharactersPasswordPolicy(PasswordPolicy):
    def __init__(
        self, character: str, min_occurrences: int, max_occurrences: int
    ) -> None:
        self.__character = character
        self.__min_occurrences = min_occurrences
        self.__max_occurrences = max_occurrences

    def validate(self, password: str) -> bool:
        return (
            self.__min_occurrences
            <= password.count(self.__character)
            <= self.__max_occurrences
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, AmountOfCharactersPasswordPolicy):
            return (
                self.__character == other.__character
                and self.__min_occurrences == other.__min_occurrences
                and self.__max_occurrences == other.__max_occurrences
            )
        return NotImplemented


class CharacterAtPositionPasswordPolicy(PasswordPolicy):
    def __init__(self, character: str, positions: List[int]) -> None:
        self.__character = character
        self.__positions = positions

    def validate(self, password: str) -> bool:
        found_once = False
        for position, character in enumerate(password):
            if character == self.__character and position + 1 in self.__positions:
                if found_once:
                    return False
                found_once = True
        return found_once

    def __eq__(self, other: object) -> bool:
        if isinstance(other, CharacterAtPositionPasswordPolicy):
            return (
                self.__character == self.__character
                and self.__positions == other.__positions
            )
        return NotImplemented


def parse_password_and_amount_of_characters_password_policy(
    password_with_policy: str,
) -> Tuple[str, PasswordPolicy]:
    policy_str, password = [part.strip() for part in password_with_policy.split(":")]

    occurrences, letter = policy_str.split(" ")
    min_occurrences, max_occurences = [int(occ) for occ in occurrences.split("-")]

    return (
        password,
        AmountOfCharactersPasswordPolicy(letter, min_occurrences, max_occurences),
    )


def parse_password_and_character_at_position_password_policy(
    password_with_policy: str,
) -> Tuple[str, PasswordPolicy]:
    policy_str, password = [part.strip() for part in password_with_policy.split(":")]

    occurrences, letter = policy_str.split(" ")
    positions = [int(occ) for occ in occurrences.split("-")]

    return (
        password,
        CharacterAtPositionPasswordPolicy(letter, positions),
    )


def get_valid_passwords(
    passwords_and_policies: List[Tuple[str, PasswordPolicy]]
) -> List[str]:
    return [
        password
        for password, policy in passwords_and_policies
        if policy.validate(password)
    ]
