from dataclasses import dataclass


@dataclass
class Editor:
    name: str

    def __str__(self):
        return f"{self.name}"
