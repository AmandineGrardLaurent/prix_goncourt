# -*- coding: utf-8 -*-

"""
Classe abstraite Person
"""

from dataclasses import dataclass, field
from abc import ABC


@dataclass
class Person(ABC):
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
