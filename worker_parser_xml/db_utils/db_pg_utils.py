"""
Методы работы с основной БД
"""
import psycopg2
from worker_parser_xml import config


class PgDb:
    conn = psycopg2.connect(**config.pg_params)

    def get_document_type_id(self, type_document, version):
        """
        Получение id типа документа
        :param type_document:  тип документа
        :param version: версия документа
        :return: id типа документа
        """
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id FROM rrd_document_dic_type WHERE title=%s AND version=%s",
                        (type_document, version))
            type_id = cur.fetchone()
            self.conn.commit()
        return type_id

    def get_feature_type_id(self, type_feature):
        """
        Получение id типа сущности
        :param type_feature: тип сущности
        :return: id типа сущности
        """
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id FROM rrd_feature_dic_type WHERE title=%s ",  (type_feature,))
            type_id = cur.fetchone()
            print('type_id_feature:', type_id)
            self.conn.commit()
        return type_id

    def rec_to_storage(self, path_zip):
        """
        Запись в storage
        :param path_zip: адрес архива, загружаемого пользователем
        :return: id созданной записи
        """
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO rrd_storage (zip, pdf) VALUES (%s, %s) RETURNING id",
                        (path_zip, path_zip))
            storage_id = cur.fetchone()[0]
            print(storage_id)
            self.conn.commit()
        print('storage_id: ', storage_id)
        return storage_id

    def rec_to_document(self, date_upload, type_id, guid, storage_id, registration_number, date_formation):
        """
        Запись в document
        :param date_upload: /данные
        :param type_id: /данные
        :param guid: /данные
        :param storage_id: /данные
        :param registration_number: /данные
        :param date_formation: /данные
        :return: id созданной записи
        """
        with self.conn:
            cur = self.conn.cursor()

            cur.execute("INSERT INTO rrd_document (guid, "
                        "registration_number, "
                        "date_formation, "
                        "date_upload, "
                        "type_id, "
                        "storage_id) "
                        "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
                        (guid,
                        registration_number,
                        date_formation,
                        date_upload,
                        type_id,
                        storage_id))
            document_id = cur.fetchone()[0]
            print(document_id)
            self.conn.commit()
        return document_id

    def rec_to_feature(self, type_id, document_id, registration_number, registration_date):
        """
        Запись в feature
        :param type_id: /данные
        :param document_id: /данные
        :param registration_number: /данные
        :param registration_date: /данные
        :return: (id созданной записи)
        """
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO rrd_feature ("
                        "registration_number, "
                        "registration_date, "
                        "document_id, "
                        "type_id) "
                        "VALUES (%s, %s, %s, %s) RETURNING id",
                        (registration_number,
                        registration_date,
                        document_id,
                        type_id))
            feature_id = cur.fetchone()[0]
            print(feature_id)
            self.conn.commit()
        #return feature_id

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    a = PgDb()
