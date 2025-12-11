# -*- coding: utf-8 -*-

from dataclasses import dataclass

import pymysql

from goncourt.daos.dao import Dao
from goncourt.models.author import Author
from goncourt.models.book import Book
from goncourt.models.editor import Editor
from goncourt.models.mainCharacter import MainCharacter

from goncourt.models.selection import Selection


@dataclass
class SelectionDao(Dao[Selection]):
    """
       Data Access Object (DAO) for the 'Selection' entity.
        This class interacts with the 'book_selection' table and manages operations related to
        book selections for the Goncourt prize, including adding books to a selection,
        reading books in a selection, reading and updating votes for a selection.
    """

    def read_selection(self, selection_nb: int) -> list[Book]:
        """
            Fetch all books for a given selection, along with their associated author, editor,
            and main characters.
        :param selection_nb: The selection number (1, 2, 3).
        :return: list[Book]: A list of books associated with the selection.
        """
        books: list[Book] = []

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:

            sql_books = """
                SELECT 
                    b.id_book, b.title, b.description, b.publication_date,
                    b.pages_nb, b.ISBN, b.price,
                    e.name AS editor_name,
                    a.biography,
                    p.last_name, p.first_name,
                    bs.id_selection
                FROM book AS b
                JOIN editor AS e 
                    ON b.id_editor = e.id_editor
                JOIN author AS a 
                    ON a.id_author = b.id_author
                JOIN person AS p 
                    ON p.id_person = a.id_person
                JOIN book_selection AS bs
                    ON bs.id_book=b.id_book
                WHERE id_selection = %s
                ORDER BY b.id_book
            """
            cursor.execute(sql_books, [selection_nb, ])
            book_rows = cursor.fetchall()

            if not book_rows:
                return []

            sql_characters = """
                SELECT id_book, name
                FROM main_character
                ORDER BY id_book
            """
            cursor.execute(sql_characters)
            char_rows = cursor.fetchall()

        # Map characters to books by their book_id
        characters_for_book: dict[int, list[MainCharacter]] = {}
        for row in char_rows:
            characters_for_book.setdefault(row['id_book'], []).append(
                MainCharacter(row['name'])
            )

        for row in book_rows:
            author = Author(
                biography=row['biography'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )

            editor = Editor(row['editor_name'])

            book = Book(
                title=row['title'],
                description=row['description'],
                publication_date=row['publication_date'],
                pages_nb=row['pages_nb'],
                ISBN=row['ISBN'],
                price=row['price'],
                author=author,
                editor=editor,
                main_character=characters_for_book.get(row['id_book'], [])
            )
            book.id_book = row['id_book']

            books.append(book)

        return books

    def add_books_to_selection(self, id_books: list[int], id_selection: int) -> bool:
        """
            Add a list of books to a specific selection with initial votes set to zero.
        :param id_books: A list of book IDs to be added to the selection.
        :param id_selection: The selection number (1, 2, 3) to which the books should be added.
        :return: bool: True if the books were successfully added to the selection, False otherwise.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = "INSERT INTO book_selection (id_book, id_selection, vote) VALUES (%s, %s, 0)"
                for id_book in id_books:
                    cursor.execute(sql, (id_book, id_selection))
            Dao.connection.commit()
            return True
        except Exception as e:
            print("Erreur:", e)
            return False

    def read_votes_selection(self, selection_nb: int) -> dict[str, int]:
        """
            Fetch the vote counts for each book in a given selection.
        :param selection_nb:  The selection number (1, 2, 3) for which the votes are to be fetched.
        :return: dict[str, int]: A dictionary where keys are book titles and values are the corresponding vote counts.
        """
        votes_selection: dict[str, int] = {}

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT 
                    b.title,
                    bs.vote
                FROM book_selection AS bs
                JOIN book AS b
                    ON b.id_book = bs.id_book
                WHERE bs.id_selection = %s
            """
            cursor.execute(sql, (selection_nb,))
            records = cursor.fetchall()

        for record in records:
            votes_selection[record["title"]] = record["vote"]

        return votes_selection

    def update_vote_selection(self, id_selection: int, votes: dict[int, int]) -> bool:
        """
            Update the votes for books in a specific selection.
        :param id_selection: The selection number (1, 2, 3) for which the votes should be updated.
        :param votes: A dictionary where keys are book IDs and values are the new vote counts.
        :return: bool: True if the votes were successfully updated, False otherwise.
        """
        with Dao.connection.cursor() as cursor:
            sql = """
                UPDATE book_selection
                SET vote = %s
                WHERE id_book = %s AND id_selection = %s
            """
            for id_book, new_vote in votes.items():
                cursor.execute(sql, (new_vote, id_book, id_selection))

        Dao.connection.commit()
        return True
