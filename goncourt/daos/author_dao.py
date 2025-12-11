# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional

import pymysql

from goncourt.daos.dao import Dao
from goncourt.models.author import Author


@dataclass
class AuthorDao(Dao[Author]):
    """
         Data Access Object (DAO) for interacting with author data in the database.
        Handles CRUD operations for authors, including retrieving, creating, and updating author information.
    """

    def read(self, id_author: int) -> Optional[Author]:
        """
            Retrieve a single author by their unique ID.
        :return: Optional[Author]: The `Author` object if found, otherwise `None`.
        """

        author: Optional[Author]
        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """\
                       SELECT p.last_name, p.first_name, a.biography, a.id_author
                       FROM person AS p
                       JOIN author AS a
                       ON p.id_person=a.id_person
                       WHERE a.id_author= %s
               """
            cursor.execute(sql, (id_author,))
            record = cursor.fetchone()
        if record is not None:
            author = Author(last_name=record['last_name'],
                            first_name=record['first_name'],
                            biography=record['biography'])
            author.id_author = record['id_author']
        else:
            author = None

        return author

    def read_all(self) -> list[Author]:
        """
            Retrieve all authors from the database.
        :return: list[Author]: A list of all `Author` objects, or an empty list if no authors exist.
        """

        authors: list[Author] = []
        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """\
                        SELECT p.last_name, p.first_name, a.biography, a.id_author
                        FROM person AS p
                        JOIN author AS a
                        ON p.id_person=a.id_person
                      """
            cursor.execute(sql)
            records = cursor.fetchall()

            if not records:
                return []
            else:
                for record in records:
                    author = Author(last_name=record['last_name'],
                                    first_name=record['first_name'],
                                    biography=record['biography'])
                    author.id_author = record['id_author']
                    authors.append(author)

                return authors
