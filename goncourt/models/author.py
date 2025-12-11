# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Optional, override

from goncourt.models.person import Person


@dataclass
class Author(Person):
    """
            This class represents an Author. It inherits from the `Person` class and
        adds specific attributes such as the author's biography.

    Attributes:
        id_author (Optional[int]): The unique identifier for the author.
        biography (str): A short biography of the author.

    Methods:
        __str__(): Override of the string representation method to return a detailed description
                   of the author's biography.
    """
    id_author: Optional[int] = field(default=None, init=False)
    biography: str

    @override
    def __str__(self):
        return (f"Biographie de {super().__str__()} : "
                f"{self.biography}")
