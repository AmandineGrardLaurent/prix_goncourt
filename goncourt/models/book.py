# -*- coding: utf-8 -*-
import datetime
import decimal
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from goncourt.models.author import Author
from goncourt.models.editor import Editor
from goncourt.models.mainCharacter import MainCharacter


@dataclass()
class Book:
    id_book: Optional[int] = field(default=None, init=False)
    title: str
    description: str
    publication_date: datetime
    pages_nb: int
    ISBN: str
    price: decimal.Decimal
    editor: Editor
    author: Author
    main_character: list[MainCharacter] = field(default_factory=list)

    def __str__(self):
        characters = ", ".join([character.name for character in self.main_character])
        return (f"Informations du livre {self.title} :\n"
                f"- Titre : {self.title}"
                f"- Résumé : {self.description}"
                f"- Personnage(s) principal(aux) : {characters}"
                f"- Date de publication : {self.publication_date}"
                f"- Nombre de pages : {self.pages_nb}"
                f"- ISBN : {self.ISBN}"
                f"- Prix : {self.price}"
                f"- Editor: {self.editor.name}")
