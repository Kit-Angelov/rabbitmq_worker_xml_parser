"""
Получает данные от handler_xml и записывает в основную БД с помощью db_pg_utils
"""
from base_functions import unzip
from db_utils.db_pg_utils import PgDb
from data_miner import MinerData
import os


class Loader:

    def __init__(self, data, path_to_zip):
        self.__loader = None
        self.__data = data
        self.__path_to_zip = path_to_zip

    def load(self):
        self.__loader = PgDb()
        storage_id = self.__loader.rec_to_storage(self.__path_to_zip)
        document_id = self.__loader.rec_to_document(self.__data.document.date_upload,
                                                    self.__data.document.type_id,
                                                    self.__data.document.guid,
                                                    storage_id,
                                                    self.__data.document.registration_number,
                                                    self.__data.document.date_formation,)

        for feature in self.__data.feature_data_list:
            location_id = self.__loader.rec_to_location(feature.location.okato,
                                                        feature.location.kladr,
                                                        feature.location.note,
                                                        feature.location.region)
            self.__loader.rec_to_feature(feature.type_id,
                                         document_id,
                                         feature.registration_number,
                                         feature.registration_date,
                                         location_id)


class MinerXML:

    def __init__(self, worker_dir, path_to_zip):
        self.worker_dir = worker_dir
        self.__path_to_zip = path_to_zip
        self.__data = None
        self.__xml = None
        self.__path_to_work_dir = None

    def __get_xml(self):
        files, self.__path_to_work_dir = unzip(self.__path_to_zip, self.worker_dir)
        for file in files:
            if str(file).endswith('xml'):
                self.__xml = os.path.join(self.__path_to_work_dir, file)

    def get_data(self):
        self.__get_xml()
        data_miner = MinerData(self.__xml)
        self.__data = data_miner.get_data()
        return self.__data

