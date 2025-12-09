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
                f"- Titre : {self.title} \n"
                f"- Résumé : {self.description} \n"
                f"- Personnage(s) principal(aux) : {characters} \n"
                f"- Date de publication : {self.publication_date} \n"
                f"- Nombre de pages : {self.pages_nb} \n"
                f"- ISBN : {self.ISBN} \n"
                f"- Prix : {self.price} euros \n"
                f"- Editeur: {self.editor.name} \n")
