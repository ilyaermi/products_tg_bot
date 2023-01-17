import sqlite3 as sl
from .classes import Expenditure, Coming
from config import db_path
from datetime import datetime
from typing import Union
import os


class Base:
    def __init__(self, connect: sl.Connection, cursor: sl.Cursor):
        self.db = connect
        self.cursor = cursor


class AdminsDatabaseConnector(Base):
    """connector to database w/ users"""

    def create_table(self):
        """Creates table if not exists."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Admin (
                                id int
                                )''')
        self.db.commit()

    def get_admins(self,) -> list[int]:
        ans = self.cursor.execute('SELECT * FROM Admin').fetchall()
        return [i[0] for i in ans]

    def add_admins(self, list_users: list[int]) -> None:
        for user_id in list_users:
            data = self.cursor.execute(
                'SELECT * FROM Admin WHERE id=?', [user_id]).fetchall()
            if len(data) == 0:
                self.cursor.execute('INSERT INTO Admin VALUES(?)',
                                    [user_id])
        self.db.commit()


class ExpendituresDatabaseConnector(Base):
    """connector to database w/ users"""

    def create_table(self):
        """Creates table if not exists."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Expenditure (
                                time int,
                                user_id int,
                                product TEXT,
                                flow_direction TEXT,
                                count FLOAT,
                                price FLOAT
                                )''')
        self.db.commit()

    def add_expenditure(self, exp: Expenditure):
        self.cursor.execute(
            'INSERT INTO Expenditure VALUES(?,?,?,?,?,?)', list(exp.__dict__.values()))
        self.db.commit()


class ComingsDatabaseConnector(Base):
    """connector to database w/ users"""

    def create_table(self):
        """Creates table if not exists."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Сoming (
                                time int,
                                user_id int,
                                product TEXT,
                                count FLOAT
                                )''')
        self.db.commit()

    def add_coming(self, com:Coming):
        self.cursor.execute(
            'INSERT INTO Сoming VALUES(?,?,?,?)', list(com.__dict__.values()))
        self.db.commit()

connect = sl.connect(db_path)
cursor = sl.Cursor(connect)
db_admins = AdminsDatabaseConnector(connect, cursor)
db_expenditures = ExpendituresDatabaseConnector(connect, cursor)
db_comings = ComingsDatabaseConnector(connect, cursor)

for db in [db_admins, db_expenditures, db_comings]:
    db.create_table()