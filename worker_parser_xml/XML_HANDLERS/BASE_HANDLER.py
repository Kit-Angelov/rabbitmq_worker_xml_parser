from xml_parse_project.worker_parser_xml.db_utils.db_sqlite_utils import SqliteDB
from xml_parse_project.worker_parser_xml.db_utils.db_pg_utils import PgDb
from uuid import uuid4
from datetime import date
import os


class Document:

    def __init__(self):
        self.guid = None
        self.date_formation = None
        self.registration_number = None
        self.date_upload = None
        self.type_id = None


class Feature:

    def __init__(self):
        self.registration_number = None
        self.registration_date = None
        self.geometry = None
        self.location = Location()
        self.childs = []
        self.type_id = None
        self.code = None


class Location:

    def __init__(self):
        self.note = None
        self.okato = None
        self.kladr = None
        self.oktmo = None
        self.region = None


class Handler:

    def __init__(self, etree, xml, code_xml):
        self.__code = code_xml
        self.document = Document()
        self.feature_data_list = []
        self.location = Location()
        self.etree = etree
        self.xml = xml
        self.context = None
        self.__get_guid()
        self.__get_date_upload()
        self.__get_document_type_id()

    def __get_guid(self):
        self.__sqlite_con = SqliteDB()
        try:
            self.document.guid = self.__sqlite_con.get_guid(os.path.basename(os.path.split(self.xml)[0]))
        except Exception as e:
            print(e)
            self.document.guid = str(uuid4())

    def __get_date_upload(self):
        self.__sqlite_con = SqliteDB()
        try:
            self.document.date_upload = self.__sqlite_con.get_date_upload(os.path.basename(os.path.split(self.xml)[0]))
        except Exception as e:
            print(e)
            self.document.date_upload = date.today()

    def __get_document_type_id(self):
        self.__pg_db_connect = PgDb()
        try:
            self.document.type_id = self.__pg_db_connect.get_document_type_id(self.__code)
        except Exception as e:
            print(e)
            self.document.type_id = str(uuid4())

    def __get_document(self):
        pass

    def __get_feature_list(self):
        pass

    def __get_location(self, feature):
        pass

    def get_data(self):
        pass

    def __del__(self):
        del self.context


