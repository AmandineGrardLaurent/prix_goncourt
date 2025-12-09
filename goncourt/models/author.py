# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Optional, override

from goncourt.models.person import Person


@dataclass
class Author(Person):
    id_author: Optional[int] = field(default=None, init=False)
    biography: str

    @override
    def __str__(self):
        return (f"Biographie de {super.__str__()} : "
                f"{self.biography}")
