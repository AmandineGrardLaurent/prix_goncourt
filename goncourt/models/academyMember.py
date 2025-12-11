# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import Optional, override

from goncourt.models.person import Person


@dataclass
class AcademyMember(Person):
    """
            This class represents an Academy Member. It inherits from the `Person` class and
        contains specific attributes and behaviors for academy members, such as whether they
        are the president or a regular member of the academy.

    Attributes:
        id_academy_member (Optional[int]): The unique identifier for the academy member.
        is_president (bool): A flag indicating whether the member is the president of the academy.

    Methods:
        __str__(): Override of the string representation method to return a detailed description
                   of the academy member's role (either "Président" or "Membre de l'académie").
    """
    id_academy_member: Optional[int] = field(default=None, init=False)
    is_president: bool

    @override
    def __str__(self):
        result = f"{super().__str__()} : "
        if self.is_president:
            result += "Président"
        else:
            result += "Membre de l'académie"
        return result
