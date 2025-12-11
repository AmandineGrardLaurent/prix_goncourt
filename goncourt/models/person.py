# -*- coding: utf-8 -*-

"""
Classe abstraite Person
"""

from dataclasses import dataclass, field
from abc import ABC


@dataclass
class Person(ABC):
    """
        This is an abstract class representing a Person. It contains the basic attributes
        of a person such as their first name and last name. This class is intended to be
        inherited by other classes that require person-related attributes (AcademyMember, Author).

        Attributes:
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.

        Methods:
            __str__(): Returns the string representation of the person's full name (first and last name).
    """
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
