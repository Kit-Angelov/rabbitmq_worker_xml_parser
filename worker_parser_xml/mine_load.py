"""
Получает данные от handler_xml и записывает в основную БД с помощью db_pg_utils
"""
from worker_parser_xml.db_utils.db_pg_utils import PgDb
from base_function import unzip
from xml_parse_project.worker_parser_xml.db_utils.db_pg_utils import PgDb
from .data_miner import MinerData
import os


class Loader:

    def __init__(self, data):
        self.__loader = PgDb()
        self.__data = data

    def load(self):
        storage_id = self.__loader.rec_to_storage(self.__data.xml)

        document_id = self.__loader.rec_to_document(self.__data.Document.date_upload,
                                                    self.__data.Document.type_id,
                                                    self.__data.Document.guid,
                                                    storage_id,
                                                    self.__data.Document.registration_number,
                                                    self.__data.Document.date_formation,)
        for feature in self.__data.feature_data_list:
            feature_id = self.__loader.rec_to_feature(feature.type_id,
                                                      document_id,
                                                      feature.registration_number,
                                                      feature.registration_date)


class MinerXML:

    def __init__(self, worker_dir, path_to_zip):
        self.worker_dir = worker_dir
        self.__path_to_zip = path_to_zip
        self.__data = None
        self.__xml = None
        self.__path_to_work_dir = None

    def __get_xml(self):
        files, path_to_work_dir = unzip(self.__path_to_zip, self.worker_dir)
        self.__path_to_work_dir = path_to_work_dir
        for file in files:
            if str(file).endswith('xml'):
                self.__xml = os.path.join(path_to_work_dir, file)

    def get_data(self):
        data_miner = MinerData(self.__xml)
        self.__data = data_miner.get_data()
        return self.__data

