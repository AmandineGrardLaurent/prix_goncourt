# -*- coding: utf-8 -*-
from typing import Optional

from goncourt.daos.author_dao import AuthorDao
from goncourt.models.author import Author


class Goncourt:

    @staticmethod
    def get_author_by_id(id_author: int) -> Optional[Author]:
        author_dao: AuthorDao = AuthorDao()
        return author_dao.read(id_author)