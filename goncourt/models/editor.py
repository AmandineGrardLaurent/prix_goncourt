from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Editor:
    id_editor: Optional[int] = field(default=None, init=False)
    name: str

    def __str__(self):
        return f"{self.name}"
