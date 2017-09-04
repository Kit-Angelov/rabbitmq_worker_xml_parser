"""
Получает данные от handler_xml и записывает в основную БД с помощью db_pg_utils
"""
import base_functions
from db_utils import db_pg_utils
import data_miner
from downloader import download_file
import os


class Loader:

    def __init__(self, data, path_to_zip):
        self.__loader = None
        self.__data = data
        self.__path_to_zip = path_to_zip

    def load(self):
        self.__loader = db_pg_utils.PgDb()
        storage_id = self.__loader.rec_to_storage(self.__path_to_zip)
        document_id = self.__loader.rec_to_document(self.__data.document.date_upload,
                                                    self.__data.document.type_id,
                                                    self.__data.document.guid,
                                                    storage_id,
                                                    self.__data.document.registration_number,
                                                    self.__data.document.date_formation)

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

    def __init__(self, worker_dir, url):
        self.worker_dir = worker_dir
        self.__url = url
        self.__path_to_zip = None
        self.__data = None
        self.__xml = None
        self.__path_to_work_dir = None

    def __download(self):
        self.__path_to_zip = download_file(self.__url, self.worker_dir)
        print('Download file {} done'.format(self.__path_to_zip))

    def __get_xml(self):
        files, self.__path_to_work_dir = base_functions.unzip(self.__path_to_zip, self.worker_dir)
        for file in files:
            if str(file).endswith('xml'):
                self.__xml = file
        print('Xml file name: {}'.format(self.__xml))

    def get_data(self):
        self.__download()
        self.__get_xml()
        miner_data = data_miner.MinerData(self.__xml, self.__path_to_work_dir)
        self.__data = miner_data.get_data()
        print('-----Data received------')
        return self.__data

