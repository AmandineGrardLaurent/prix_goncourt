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

    def read_selection(self, selection_nb: int) -> list[Book]:
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
