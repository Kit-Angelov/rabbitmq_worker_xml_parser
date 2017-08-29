from lxml.etree import QName
from .BASE_HANDLER import Handler, Feature
from xml_parse_project.worker_parser_xml.db_utils.db_pg_utils import PgDb
from xml_parse_project.worker_parser_xml.XML_HANDLERS.handler_utils import (get_document,
                                                                            get_location,
                                                                            get_feature_parcel)


class HandlerZU(Handler):

    def __init__(self, etree, xml, code):
        super().__init__(etree, xml, code)

    def __get_document(self):
        get_document(self)

    def __get_feature_list(self):
        self.__pg_db_connect = PgDb()
        self.context = self.etree.iterparse(self.xml, events=("end",))
        for event, elem in self.context:
            if QName(elem.tag).localname == 'Parcel':
                feature = get_feature_parcel(elem, self.__pg_db_connect)
                self.feature_data_list.append(feature)

    def get_data(self):
        self.__get_document()
        self.__get_feature_list()


class HandlerKVZU7(HandlerZU):
    pass


class HandlerKPZU6(HandlerZU):
    pass


class HandlerKPT10(Handler):

    def __init__(self, etree, xml, code):
        super().__init__(etree, xml, code)

    def __get_document(self):
        get_document(self)

    def __get_feature_list(self):
        self.__pg_db_connect = PgDb()
        self.context = self.etree.iterparse(self.xml, events=("end",))
        for event, elem in self.context:
            if QName(elem.tag).localname == 'Parcel':
                feature = get_feature_parcel(elem, self.__pg_db_connect)
                self.feature_data_list.append(feature)
            if QName(elem.tag).localname == 'Parcel':
                feature = get_feature_parcel(elem, self.__pg_db_connect)
                self.feature_data_list.append(feature)
            if QName(elem.tag).localname == 'Parcel':
                feature = get_feature_parcel(elem, self.__pg_db_connect)
                self.feature_data_list.append(feature)
            if QName(elem.tag).localname == 'Parcel':
                feature = get_feature_parcel(elem, self.__pg_db_connect)
                self.feature_data_list.append(feature)
            if QName(elem.tag).localname == 'Parcel':
                feature = get_feature_parcel(elem, self.__pg_db_connect)
                self.feature_data_list.append(feature)