from dataclasses import dataclass


@dataclass
class AcademyMember:
    is_president: bool

    def __str__(self):
        result = f"Status de {super.__str__()} : "
        if self.is_president:
            result += "Président"
        else:
            result += "Membre de l'académie"
        return result
