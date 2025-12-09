# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import Optional, override

from goncourt.models.person import Person


@dataclass
class AcademyMember(Person):
    id_academy_member: Optional[int] = field(default=None, init=False)
    is_president: bool

    @override
    def __str__(self):
        result = f"Statut de {super().__str__()} : "
        if self.is_president:
            result += "Président"
        else:
            result += "Membre de l'académie"
        return result
