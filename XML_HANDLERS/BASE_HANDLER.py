from worker_parser_xml.db_utils import db_pg_client_utils
from worker_parser_xml.db_utils import db_pg_utils
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

    def __init__(self, etree, xml, work_dir, code_xml):
        self.work_dir = work_dir
        self.__code = code_xml
        self.document = Document()
        self.feature_data_list = []
        self.location = Location()
        self.etree = etree
        self.xml = xml
        self.context = None
        self.pg_db_connect = db_pg_utils.PgDb()
        self.pg_db_client_connect = db_pg_client_utils.PgDb()
        self.get_guid()
        self.get_date_upload()
        self.get_document_type_id()

    def get_guid(self):
        try:
            self.document.guid = self.pg_db_client_connect.get_guid(os.path.basename(os.path.split(self.work_dir)[-1]))
            print('Document guid: {}'.format(self.document.guid))
        except Exception as e:
            print('Error: ', e)
            self.document.guid = str(uuid4())

    def get_date_upload(self):
        try:
            self.document.date_upload = self.pg_db_client_connect.get_date_upload(os.path.basename
                                                                                  (os.path.split(self.work_dir)[-1]))
            print('Document date upload: {}'.format(self.document.date_upload))
        except Exception as e:
            print('Error: ', e)
            self.document.date_upload = date.today()

    def get_document_type_id(self):
        try:
            self.document.type_id = self.pg_db_connect.get_document_type_id(self.__code)
            print('Document type id: {}'.format(self.document.type_id))
        except Exception as e:
            print('Error: ', e)
            self.document.type_id = str(uuid4())

    def get_document(self):
        pass

    def get_feature_list(self):
        pass

    def get_location(self, feature):
        pass

    def get_data(self):
        self.get_document()
        self.get_feature_list()

    def __del__(self):
        del self.context

