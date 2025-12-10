# -*- coding: utf-8 -*-

"""
Classe abstraite générique Dao[T], dont hérite les classes de DAO de chaque entité
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar, Optional
import pymysql.cursors


@dataclass
class Dao[T](ABC):
    connection: ClassVar[pymysql.Connection] = \
        pymysql.connect(host='localhost',
                        user='prix_goncourt',
                        password='GstfTqPZ1/VhMqAP',
                        database='prix_goncourt',
                        cursorclass=pymysql.cursors.DictCursor)



