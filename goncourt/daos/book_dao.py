# -*- coding: utf-8 -*-

import decimal
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from goncourt.daos.dao import Dao
from goncourt.models.author import Author
from goncourt.models.book import Book


@dataclass
class BookDao(Dao[Book]):

    @staticmethod
    def init_book_db(record):
        book: Book = Book(record['title'], record['description'], record['publication_date', record['pages_nb'], record['ISBN'], record['price'])
        book.author: Author = Author(record['last_name'], record['first_name'])


    def read(self, id_book: int) -> Optional[Book]:

        book: Optional[Book]

        with Dao.connection.cursor() as cursor:
            sql = """\
                SELECT b.title, b.description, b.publication_date, b.pages_nb, b.ISBN, b.price, m.name, e.name, a.biography, p.last_name, p.first_name 
                FROM book AS b
                RIGHT JOIN main_character AS m
                ON m.id_book=b.id_book
                JOIN editor AS e
                ON b.id_editor=e.id_editor
                JOIN author AS a
                ON a.id_author=b.id_author
                JOIN person AS p
                ON p.id_person=a.id_person
                WHERE b.id_book= %s
        """
            cursor.execute(sql, (id_book,))
            record = cursor.fetchone()
        if record is not None:
            book = self.teacher_from_db(record)
        else:
            book = None

        return book
