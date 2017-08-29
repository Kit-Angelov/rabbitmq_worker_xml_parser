from lxml.etree import QName
from .BASE_HANDLER import Handler, Feature
#from xml_parse_project.worker_parser_xml.XML_HANDLERS.config_handlers import type_feature
from xml_parse_project.worker_parser_xml.db_utils.db_pg_utils import PgDb


class HandlerZU(Handler):

    def __init__(self, etree, xml, code):
        super().__init__(etree, xml, code)
        self.__etree = etree
        self.__code_feature = 'Parcel'

    def __get_document(self):
        self.__context = self.__etree.iterparse(self.xml, events=("end",))
        for event, elem in self.__context:
            if QName(elem.tag).localname == 'Date':
                if elem.text not in ['\n', '', ' ']:
                    self.document.date_formation = elem.text
            if QName(elem.tag).localname == 'Number':
                if elem.text not in ['\n', '', ' ']:
                    self.document.registration_number = elem.text

    def __get_feature_list(self):
        self.__pg_db_connect = PgDb()
        self.__context = self.__etree.iterparse(self.xml, events=("end",))
        for event, elem in self.__context:
            if QName(elem.tag).localname == 'Parcel':
                feature = Feature()
                self.__get_location(feature)
                try:
                    parcel_data = dict(zip(elem.keys(), elem.values()))
                    feature.registration_number = parcel_data.pop('CadastralNumber')
                    feature.registration_date = parcel_data.pop('DateCreated')
                    feature.type_id = self.__pg_db_connect.get_feature_type_id(self.__code_feature)
                    self.feature_data_list.append(feature)
                except Exception as e:
                    print('ERRORRRR', e)
                    continue

    def __get_location(self, feature):
        self.__context = self.__etree.iterparse(self.xml, events=("end",))
        for event, elem in self.__context:
            if QName(elem.tag).localname == 'OKATO':
                feature.location.okato = elem.text
            if QName(elem.tag).localname == 'KLADR':
                feature.location.kladr = elem.text
            if QName(elem.tag).localname == 'Note':
                feature.location.note = elem.text
            if QName(elem.tag).localname == 'Region':
                feature.location.region = elem.text

    def get_data(self):
        self.__get_document()
        self.__get_feature_list()


class HandlerKVZU7(HandlerZU):
    pass


class HandlerKPZU6(HandlerZU):
    pass
