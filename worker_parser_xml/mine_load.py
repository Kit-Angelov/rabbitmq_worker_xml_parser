"""
Получает данные от handler_xml и записывает в основную БД с помощью db_pg_utils
"""
from worker_parser_xml.handler_xml import parser_xml
from worker_parser_xml.db_utils.db_sqlite_utils import SqliteDB
from worker_parser_xml.db_utils.db_pg_utils import PgDb
from worker_parser_xml import config


class Loaderqqq:

    def __init__(self, path_to_zip):
        self.path_zip = path_to_zip
        self.pg_db_connect = PgDb()

    # получение данных о документе и сущностях
    def get_data(self, abs_path_zip):
        """

        :param path_zip: адрес архива, загружаемого пользователем
        :return: данные полученные из xml, guid записи в базе КПП, дата загрузки архива пользователем
        """
        data = parser_xml(abs_path_zip)
        sqlite_con = SqliteDB()
        guid = sqlite_con.get_guid(self.path_zip)
        date_upload = sqlite_con.get_date_upload(self.path_zip)
        sqlite_con.close()
        return data, guid, date_upload


    # получение document_type_id
    def __get_doc_type_id(pg_db_connect, type_document, version_document):
        """

        :param pg_db_connect: соединение с бд
        :param type_document: тип документа, взятый из данных полученных из xml
        :param version_document: версия документа, взятая из данных полученных из xml
        :return: id типа документа
        """
        return pg_db_connect.get_document_type_id(type_document, version_document)

    """
    Здесь какая то логика работы с сущностями, а именно:
    изьятия всех сущностей из полученных данных,
    определение их типа,
    определение их состава,
    использование полученной информации для добавления записи в таблицу feature
    """
    ################################################################################


    # определение кол-ва и списка feature
    def __get_name_feature(data):
        """
        Определение списка имен сущностей документа и их кол-ва
        :param data: данные полученные из xml
        :return: списко имен сущностей документа и их число
        """
        count = 0
        list_feature_name = []
        for item in data.keys():
            for tag in config.feature_tags:
                if item.startswith(tag):
                    list_feature_name.append(item)
                    count += 0
        return list_feature_name, count


    # определение типа feature и
    # получение feature_type_id
    def __get_feature_type_id(pg_db_connect, *args):
        """
        Определение типа конкретной сущности
        :param pg_db_connect: соединение с бд
        :param args: кортеж признаков определяющих тип сущности
        :return: id типа сущности
        """
        feature_type = config.type_feature_dict[args[0]]
        print('feature_type:', feature_type)
        print('feature_type:', type(feature_type))
        return pg_db_connect.get_feature_type_id(feature_type)


    # получение данных о определенном feature из data
    def __get_feature_data(data, feature_name):
        """
        Получение данных о сущности из дата в виде словаря
        :param data: данные полученные из xml
        :param feature_name: имя сущности в data
        :return: словарь описывающий определенную сущность
        """
        return data[feature_name]
    ################################################################################


    # запись в storage и получение storage_id
    def __rec_to_storage(pg_db_connect, path_zip):
        """
        Запись в storage
        :param pg_db_connect: соединение с бд
        :param path_zip: адрес архива, загружаемого пользователем
        :return: id созданной записи
        """
        return pg_db_connect.rec_to_storage(path_zip)


    # запись document
    def __rec_to_document(pg_db_connect, date_upload, type_id, guid, storage_id, registration_number, date_formation):
        """
        Запись документа
        :param pg_db_connect: соединение с бд
        :param date_upload: /данные
        :param type_id: /данные
        :param guid: /данные
        :param storage_id: /данные
        :param registration_number: /данные
        :param date_formation: /данные
        :return: id созданной записи
        """
        return pg_db_connect.rec_to_document(date_upload, type_id, guid, storage_id, registration_number, date_formation)


    # запись feature
    def __rec_to_feature(pg_db_connect, type_id, document_id, registration_number, registration_date):
        """
        Запись сущности
        :param pg_db_connect: соединение с бд
        :param type_id: /данные
        :param document_id: /данные
        :param registration_number: /данные
        :param registration_date: /данные
        :return:
        """
        pg_db_connect.rec_to_feature(type_id, document_id, registration_number, registration_date)

    # основная функция
    def main(self, abs_path_zip):
        """
        Собственно главная функция для обработки xml
        :param path_zip:
        :return:
        """
        data, guid, date_upload = get_data(path_zip, abs_path_zip)
        print('guid:', guid)
        doc_type_id = get_doc_type_id(pg_db_connect, data['type'], data['version'])
        feature_type_id = get_feature_type_id(pg_db_connect, *(data['type'],))
        print('feature_type_id:', feature_type_id)
        storage_id = rec_to_storage(pg_db_connect, abs_path_zip)
        document_id = rec_to_document(pg_db_connect,
                                      date_upload,
                                      doc_type_id,
                                      guid,
                                      storage_id,
                                      data['registration_number'],
                                      data['date_formation'])
        list_feature_name, count = get_name_feature(data)
        for feature_name in list_feature_name:
            feature_data = get_feature_data(data, feature_name)
            rec_to_feature(pg_db_connect,
                           feature_type_id,
                           document_id,
                           feature_data['registration_number'],
                           feature_data['registration_date'])
        pg_db_connect.close()

if __name__ == '__main__':
    main('parse.zip')



from base_function import unzip
from .type_and_version_checker import TypeVersionChecker
from lxml import etree
import os
from . import config


class Loader:

    def __init__(self):
        self.pg_db_connect = PgDb()
        self.__data = None

    def load(self, data):
        self.__data = data
        return self.__data


class Miner:

    def __init__(self, base_path):
        self.base_path = base_path
        self.__path_to_zip = None
        self.__data = None
        self.__xml = None
        self.__path_to_work_dir = None

    def __get_xml(self, path_to_zip):
        self.__path_to_zip = path_to_zip
        files, path_to_work_dir = unzip(self.__path_to_zip, self.base_path)
        self.__path_to_work_dir = path_to_work_dir
        for file in files:
            if str(file).endswith('xml'):
                self.__xml = os.path.join(path_to_work_dir, file)

    def get_data(self, path_to_zip):
        self.__get_xml(path_to_zip)
        data_miner = DataMiner()
        self.__data = data_miner.get_data(self.__xml, type_xml, version_xml)
        return self.__data

