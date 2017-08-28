from lxml.etree import QName
from .BASE_HANDLER import Handler, Feature
from xml_parse_project.worker_parser_xml.XML_HANDLERS.config_handlers import type_feature
from xml_parse_project.worker_parser_xml.db_utils.db_pg_utils import PgDb


class HandlerKVZU7(Handler):

    def __init__(self, etree, xml, code_xml):
        super().__init__(etree, xml, code_xml)
        #self.xml = xml
        self.__etree = etree
        self.__code = code_xml
        self.__pg_db_connect = PgDb()

    def __get_document(self):
        self.__context = self.__etree.iterparse(self.xml, events=("end",))
        for event, elem in self.__context:
            if QName(elem.tag).localname == 'Date':
                if elem.text not in ['\n', '', ' ']:
                    self.document.date_formation = elem.text
            if QName(elem.tag).localname == 'Number':
                if elem.text not in ['\n', '', ' ']:
                    print('REGIS NUMBER',elem.text)
                    self.document.registration_number = elem.text

    def __get_feature_list(self):
        self.__context = self.__etree.iterparse(self.xml, events=("end",))
        for event, elem in self.__context:
            if QName(elem.tag).localname == 'Parcel':
                feature = Feature()
                print('FEATURE', feature)
                try:
                    parcel_data = dict(zip(elem.keys(), elem.values()))
                    feature.registration_number = parcel_data.pop('CadastralNumber')
                    print('feature.registration_number', feature.registration_number)
                    feature.registration_date = parcel_data.pop('DateCreated')
                    print('feature.registration_date', feature.registration_date)
                    feature_type = type_feature[self.__code]
                    feature.type_id = self.__pg_db_connect.get_feature_type_id(feature_type)
                    print('feature.type_id', feature.type_id)
                    self.feature_data_list.append(feature)
                    print('FEATURE_LIST', self.feature_data_list)
                except Exception as e:
                    print('ERRORRRR',e)
                    continue

    def __get_location(self):
        pass

    def get_data(self):
        self.__get_document()
        self.__get_feature_list()
        self.__get_location()
