# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Selection:
    id_selection: Optional[int] = field(default=None, init=False)
    date: datetime
    selection_nb: int

    def __str__(self):
        return f"Selection {self.selection_nb} en date du {self.date} : "
