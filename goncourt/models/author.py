# -*- coding: utf-8 -*-
from dataclasses import dataclass

from goncourt.models.person import Person


@dataclass
class Author(Person):
    biography: str

    def __str__(self):
        return (f"Biographie de {super.__str__()} : "
                f"{self.biography}")
