from xml_parse_project.worker_parser_xml.db_utils.db_sqlite_utils import SqliteDB
from xml_parse_project.worker_parser_xml.db_utils.db_pg_utils import PgDb
from uuid import uuid4
from datetime import date


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
        self.location = None
        self.childs = []
        self.type_id = None


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
        self.Location = Location()
        self.__etree = etree
        self.xml = xml
        self.__context = self.__etree.iterparse(self.xml, events=("end",))
        self.__sqlite_con = SqliteDB()
        self.__pg_db_connect = PgDb()
        self.__get_data()

    def __get_guid(self):
        try:
            self.document.guid = self.__sqlite_con.get_guid(self.xml)
        except Exception as e:
            print(e)
            self.document.guid = uuid4()

    def __get_date_upload(self):
        try:
            self.document.date_upload = self.__sqlite_con.get_date_upload(self.xml)
        except Exception as e:
            print(e)
            self.document.date_upload = date.today()

    def __get_document_type_id(self):
        try:
            self.document.type_id = self.__pg_db_connect.get_document_type_id(self.__code)
        except Exception as e:
            print(e)
            self.__code = uuid4()

    def __get_document(self):
        pass

    def __get_feature_list(self):
        pass

    def __get_location(self):
        pass

    def __get_data(self):
        self.__get_document_type_id()
        self.__get_guid()
        self.__get_date_upload()
        self.__get_document()
        self.__get_feature_list()
        self.__get_location()
        return self

    def __del__(self):
        self.__sqlite_con.close()
        self.__pg_db_connect.close()
        del self.__context


