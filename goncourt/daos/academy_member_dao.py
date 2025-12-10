# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional

import pymysql

from goncourt.daos.dao import Dao
from goncourt.models.academyMember import AcademyMember


@dataclass
class AcademyMemberDao(Dao[AcademyMember]):
    def read(self, id_academy_member: int) -> Optional[AcademyMember]:

        academy_member: Optional[AcademyMember]
        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """\
                    SELECT p.last_name, p.first_name, 
                    am.id_academy_member, am.is_president
                    FROM person AS p
                    JOIN academy_member AS am
                        ON p.id_person=am.id_person
                    WHERE am.id_academy_member= %s
               """
            cursor.execute(sql, (id_academy_member,))
            record = cursor.fetchone()
        if record is not None:
            academy_member = AcademyMember(last_name=record['last_name'],
                                           first_name=record['first_name'],
                                           is_president=record['is_president'])
            academy_member.id_academy_member = record['id_academy_member']
        else:
            academy_member = None

        return academy_member

    def read_all(self) -> list[AcademyMember]:

        academy_members: list[AcademyMember] = []
        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """\
                    SELECT p.last_name, p.first_name, 
                    am.id_academy_member, am.is_president
                    FROM person AS p
                    JOIN academy_member AS am
                       ON p.id_person=am.id_person
                      """
            cursor.execute(sql)
            records = cursor.fetchall()

            if not records:
                return []
            else:
                for record in records:
                    academy_member = AcademyMember(last_name=record['last_name'],
                                                   first_name=record['first_name'],
                                                   is_president=record['is_president'])
                    academy_member.id_academy_member = record['id_academy_member']
                    academy_members.append(academy_member)

                return academy_members

    def is_president(self, lastname: str) -> bool:
        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """\
                    SELECT am.is_president
                    FROM academy_member AS am
                    JOIN person AS p
                        ON p.id_person=am.id_person
                    WHERE p.last_name= %s
               """
            cursor.execute(sql, (lastname,))
            record = cursor.fetchone()

        return record['is_president']
