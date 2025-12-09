from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AcademyMember:
    id_academy_member: Optional[int] = field(default=None, init=False)
    is_president: bool

    def __str__(self):
        result = f"Status de {super.__str__()} : "
        if self.is_president:
            result += "Président"
        else:
            result += "Membre de l'académie"
        return result
