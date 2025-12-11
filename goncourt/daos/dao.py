# -*- coding: utf-8 -*-

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar, Optional
import pymysql.cursors


@dataclass
class Dao[T](ABC):
    """
        Abstract base class for Data Access Objects (DAOs). Provides a generic interface
        for interacting with the database and managing connections.

        The DAO class establishes a connection to the database and provides the basic
        functionality required for CRUD operations. Specific DAOs for each entity (e.g.,
        `AuthorDao`, `BookDao`) inherit from this class and implement the necessary
        database interaction logic.
    """
    connection: ClassVar[pymysql.Connection] = \
        pymysql.connect(host='localhost',
                        user='prix_goncourt',
                        password='GstfTqPZ1/VhMqAP',
                        database='prix_goncourt',
                        cursorclass=pymysql.cursors.DictCursor)



