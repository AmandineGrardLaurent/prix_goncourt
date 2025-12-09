# -*- coding: utf-8 -*-
from typing import Optional

from goncourt.daos.author_dao import AuthorDao
from goncourt.daos.book_dao import BookDao
from goncourt.models.author import Author
from goncourt.models.book import Book


class Goncourt:

    @staticmethod
    def get_author_by_id(id_author: int) -> Optional[Author]:
        author_dao: AuthorDao = AuthorDao()
        return author_dao.read(id_author)

    @staticmethod
    def get_all_authors() -> list[Author]:
        author_dao: AuthorDao = AuthorDao()
        return author_dao.read_all()

    @staticmethod
    def get_book_by_id(id_book: int) -> Optional[Book]:
        book_dao: BookDao = BookDao()
        return book_dao.read(id_book)
