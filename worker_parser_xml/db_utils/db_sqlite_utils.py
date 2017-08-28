"""
Методы работы с КПП БД
"""
import sqlite3
from xml_parse_project.worker_parser_xml.db_utils.config_db import sqlite_params


class SqliteDB:

    con = sqlite3.connect(sqlite_params)

    def get_owner(self, path_zip):
        """
        Получение id владельца записи
        :param path_zip: адрес архива, загружаемого пользователем
        :return: if владельца записи
        """
        with self.con:
            cur = self.con.cursor()
            cur.execute('SELECT user_id FROM rabbit_test_rabbit WHERE file LIKE "%{0}%"'.format(path_zip))
            data = cur.fetchone()[0]
            return data

    def get_guid(self, path_zip):
        """
        Получение guid записи
        :param path_zip: адрес архива, загружаемого пользователем
        :return: guid записи
        """
        with self.con:
            cur = self.con.cursor()
            cur.execute('SELECT guid FROM rabbit_test_rabbit WHERE file LIKE "%{0}%"'.format(path_zip))
            data = cur.fetchone()[0]
            print('guid: ', data)
            return data

    def get_date_upload(self, path_zip):
        """
        Получение даты загрузки файла
        :param path_zip: адрес архива, загружаемого пользователем
        :return: дата загрузки файла
        """
        with self.con:
            cur = self.con.cursor()
            cur.execute('SELECT date_upload FROM rabbit_test_rabbit WHERE file LIKE "%{0}%"'.format(path_zip))
            data = cur.fetchone()[0]
            print('data_upload:', data)
            return data

    def close(self):
        self.con.close()
