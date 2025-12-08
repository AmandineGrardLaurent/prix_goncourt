# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import Optional


class MainCharacter:
    id_main_character: Optional[int] = field(default=None, init=False)
    name: str

    def __str__(self):
        return f"{self.name}"
