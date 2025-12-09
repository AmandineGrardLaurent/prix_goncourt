# -*- coding: utf-8 -*-
from typing import Optional

from goncourt.daos.academy_member_dao import AcademyMemberDao
from goncourt.daos.author_dao import AuthorDao
from goncourt.daos.book_dao import BookDao
from goncourt.daos.selection_dao import SelectionDao
from goncourt.models.academyMember import AcademyMember
from goncourt.models.author import Author
from goncourt.models.book import Book


class Goncourt:
    author_dao: AuthorDao = AuthorDao()
    book_dao: BookDao = BookDao()
    selection_dao: SelectionDao = SelectionDao()
    academy_member_dao: AcademyMemberDao = AcademyMemberDao()

    @staticmethod
    def get_author_by_id(id_author: int) -> Optional[Author]:
        return Goncourt.author_dao.read(id_author)

    @staticmethod
    def get_all_authors() -> list[Author]:
        return Goncourt.author_dao.read_all()

    @staticmethod
    def get_book_by_id(id_book: int) -> Optional[Book]:
        return Goncourt.book_dao.read(id_book)

    @staticmethod
    def get_books_selection(selection_nb: int) -> list[Book]:
        return Goncourt.selection_dao.read_selection(selection_nb)

    @staticmethod
    def set_books_selection(id_books: list[int], id_selection: int) -> bool:
        return Goncourt.selection_dao.add_books_to_selection(id_books, id_selection)

    @staticmethod
    def get_academy_member_by_id(id_academy_member: int) -> Optional[AcademyMember]:
        return Goncourt.academy_member_dao.read(id_academy_member)

    @staticmethod
    def get_all_academy_members() -> list[AcademyMember]:
        return Goncourt.academy_member_dao.read_all()