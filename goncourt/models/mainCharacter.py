# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Optional


@dataclass()
class MainCharacter:
    """
        This class represents the main character of a book. It contains the name of the character
        and an optional identifier. The character's name is typically used to display the main characters
        of a book.

        Attributes:
            id_main_character (Optional[int]): The unique identifier for the main character.
            name (str): The name of the main character.

        Methods:
            __str__(): Override of the string representation method to return the character's name.
    """
    id_main_character: Optional[int] = field(default=None, init=False)
    name: str

    def __str__(self):
        return f"{self.name}"
