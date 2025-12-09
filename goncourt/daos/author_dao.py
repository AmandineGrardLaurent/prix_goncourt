# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional

import pymysql

from goncourt.daos.dao import Dao
from goncourt.models.author import Author


@dataclass
class AuthorDao(Dao[Author]):
    def read(self, id_author: int) -> Optional[Author]:

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
            author = Author(record['last_name'],
                            record['first_name'],
                            record['biography'])
            author.id_author = record['id_author']
        else:
            author = None

        return author

    def read_all(self) -> list[Author]:
        return []