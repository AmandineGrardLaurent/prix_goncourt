# -*- coding: utf-8 -*-

import decimal
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

import pymysql

from goncourt.daos.dao import Dao
from goncourt.models.author import Author
from goncourt.models.book import Book
from goncourt.models.editor import Editor
from goncourt.models.mainCharacter import MainCharacter


@dataclass
class BookDao(Dao[Book]):

    def read(self, id_book: int) -> Optional[Book]:
        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT 
                    b.id_book, b.title, b.description, b.publication_date,
                    b.pages_nb, b.ISBN, b.price,
                    m.name AS character_name,
                    e.name AS editor_name,
                    a.biography,
                    p.last_name, p.first_name
                FROM book AS b
                JOIN main_character AS m 
                    ON m.id_book = b.id_book
                JOIN editor AS e 
                    ON b.id_editor = e.id_editor
                JOIN author AS a 
                    ON a.id_author = b.id_author
                JOIN person AS p 
                    ON p.id_person = a.id_person
                WHERE b.id_book = %s
            """
            cursor.execute(sql, (id_book,))
            records = cursor.fetchall()

        if not records:
            return None

        record = records[0]

        author = Author(
            biography=record['biography'],
            first_name=record['first_name'],
            last_name=record['last_name']
        )

        editor = Editor(
            name=record['editor_name']
        )

        main_characters = [MainCharacter(row['character_name']) for row in records]

        book = Book(
            title=record['title'],
            description=record['description'],
            publication_date=record['publication_date'],
            pages_nb=record['pages_nb'],
            ISBN=record['ISBN'],
            price=record['price'],
            editor=editor,
            author=author,
            main_character=main_characters
        )
        book.id_book = record['id_book']
        return book

    def read_all(self) -> list[Book]:
        books: list[Book] = []

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:

            sql_books = """
                SELECT 
                    b.id_book, b.title, b.description, b.publication_date,
                    b.pages_nb, b.ISBN, b.price,
                    e.name AS editor_name,
                    a.biography,
                    p.last_name, p.first_name
                FROM book AS b
                JOIN editor AS e 
                    ON b.id_editor = e.id_editor
                JOIN author AS a 
                    ON a.id_author = b.id_author
                JOIN person AS p 
                    ON p.id_person = a.id_person
                ORDER BY b.id_book
            """
            cursor.execute(sql_books)
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
