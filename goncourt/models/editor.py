from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Editor:
    """
        This class represents an Editor entity. It contains the name of the editor
        and an optional identifier. The editor's name can be used to display the editor
        of a book, for example.

        Attributes:
            id_editor (Optional[int]): The unique identifier for the editor.
            name (str): The name of the editor.

        Methods:
            __str__(): Override of the string representation method to return the editor's name.
    """
    id_editor: Optional[int] = field(default=None, init=False)
    name: str

    def __str__(self):
        return f"{self.name}"
