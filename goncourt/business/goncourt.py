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
    """
        The Goncourt class acts as a business logic layer that interacts with the data access objects (DAOs)
        for managing the Goncourt prize selection process, including authors, books, academy members, and votes.

        It provides methods to access, update, and verify data related to books, authors, academy members, and selections.

        Attributes:
            author_dao (AuthorDao): DAO responsible for handling author data.
            book_dao (BookDao): DAO responsible for handling book data.
            selection_dao (SelectionDao): DAO responsible for handling book selections and votes.
            academy_member_dao (AcademyMemberDao): DAO responsible for handling academy member data.
    """
    author_dao: AuthorDao = AuthorDao()
    book_dao: BookDao = BookDao()
    selection_dao: SelectionDao = SelectionDao()
    academy_member_dao: AcademyMemberDao = AcademyMemberDao()

    @staticmethod
    def get_votes_selection(selection_nb: int) -> dict[str, int]:
        """
            Retrieve the vote counts for books in a specific selection.
        :return: dict[str, int]: A dictionary where the keys are book titles and the values are vote counts.
        """
        return Goncourt.selection_dao.read_votes_selection(selection_nb)

    @staticmethod
    def get_author_by_id(id_author: int) -> Optional[Author]:
        """
            Retrieve an author by their unique ID.
        :return: Optional[Author]: The author object if found, otherwise None.
        """
        return Goncourt.author_dao.read(id_author)

    @staticmethod
    def get_all_authors() -> list[Author]:
        """
             Retrieve a list of all authors.
        :return: list[Author]: A list of all authors.
        """
        return Goncourt.author_dao.read_all()

    @staticmethod
    def get_book_by_id(id_book: int) -> Optional[Book]:
        """
             Retrieve a book by its unique ID.
        :return: Optional[Book]: The book object if found, otherwise None.
        """
        return Goncourt.book_dao.read(id_book)

    @staticmethod
    def get_books_selection(selection_nb: int) -> list[Book]:
        """
             Retrieve a list of books for a specific selection.
        :param: selection_nb (int): The selection number (e.g., 1, 2, 3).
        :return: list[Book]: A list of books associated with the specified selection.
        """
        return Goncourt.selection_dao.read_selection(selection_nb)

    @staticmethod
    def set_books_selection(id_books: list[int], id_selection: int) -> bool:
        """
            Assign a list of books to a specific selection.
        :param id_books: id_books (list[int]): List of book IDs to assign to the selection.
        :param id_selection: id_selection (int): The selection number to which the books should be added.
        :return: bool: True if the operation was successful, False otherwise.
        """
        return Goncourt.selection_dao.add_books_to_selection(id_books, id_selection)

    @staticmethod
    def get_academy_member_by_id(id_academy_member: int) -> Optional[AcademyMember]:
        """
            Retrieve an academy member by their unique ID.
        :return: Optional[AcademyMember]: The academy member object if found, otherwise None.
        """
        return Goncourt.academy_member_dao.read(id_academy_member)

    @staticmethod
    def get_all_academy_members() -> list[AcademyMember]:
        """
            Retrieve a list of all academy members.
        :return: list[AcademyMember]: A list of all academy members.
        """
        print(Goncourt.academy_member_dao.read_all())
        return Goncourt.academy_member_dao.read_all()

    @staticmethod
    def verify_is_academy_member(lastname: str) -> bool:
        """
            Verify if a given person is an academy member based on their last name.
        :param lastname: lastname (str): The last name of the person to check.
        :return: bool: True if the person is an academy member, False otherwise.
        """
        return lastname in [member.last_name for member in Goncourt.academy_member_dao.read_all()]

    @staticmethod
    def verify_is_president(lastname: str) -> bool:
        """
            Verify if a given person is the president of the academy based on their last name.
        :param lastname: The last name of the person to check.
        :return: bool: True if the person is the president, False otherwise.
        """
        return Goncourt.academy_member_dao.is_president(lastname)
