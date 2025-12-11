# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Selection:
    """
        Class representing a book selection, typically used for literary awards.
        A selection is associated with a specific date and a selection number.

        Attributes:
            id_selection (Optional[int]): The unique identifier for the selection.
            date (datetime): The date the selection was made.
            selection_nb (int): The number of the selection (1st, 2nd, 3rd).

        Methods:
            __str__(): Returns a string representation of the selection's number and date.
    """
    id_selection: Optional[int] = field(default=None, init=False)
    date: datetime
    selection_nb: int

    def __str__(self):
        return f"Selection {self.selection_nb} en date du {self.date} : "
