from lxml.etree import QName
from .BASE_HANDLER import Handler
from xml_parse_project.worker_parser_xml.db_utils.db_pg_utils import PgDb
from xml_parse_project.worker_parser_xml.XML_HANDLERS.handler_utils import (get_document,
                                                                            GetterFeature)


class HandlerZU(Handler):

    def __init__(self, etree, xml, code):
        super().__init__(etree, xml, code)

    def __get_document(self):
        get_document(self)

    def __get_feature_list(self):
        self.context = self.etree.iterparse(self.xml, events=("end",))
        feature_name_list = ['Parcels', 'ObjectsRealty', 'OMSPoints', 'SpatialData', 'Bounds', 'Zones']
        feature_names = ['Parcel', 'ObjectRealty', 'OMSPoint', 'SpatialData', 'Bound', 'Zone']
        for event, elem in self.context:
            elem_tag = QName(elem.tag).localname
            if elem_tag in feature_name_list:
                for child in elem.getchildren():
                    child_tag = QName(elem.tag).localname
                    if child_tag in feature_names:
                        feature = GetterFeature().get_feature(child, self.pg_db_connect)
                        self.feature_data_list.append(feature)

    def get_data(self):
        self.__get_document()
        self.__get_feature_list()


class HandlerKVZU7(HandlerZU):

    def __get_feature_list(self):
        self.pg_db_connect = PgDb()
        self.context = self.etree.iterparse(self.xml, events=("end",))
        for event, elem in self.context:
            elem_tag = QName(elem.tag).localname
            if elem_tag == 'Parcels':
                for child in elem.getchildren():
                    child_tag = QName(child.tag).localname
                    if child_tag == 'Parcel':
                        feature = GetterFeature().get_feature(child, self.pg_db_connect)
                        self.feature_data_list.append(feature)


class HandlerKPZU6(HandlerZU):

    def __get_feature_list(self):
        self.pg_db_connect = PgDb()
        self.context = self.etree.iterparse(self.xml, events=("end",))
        for event, elem in self.context:
            elem_tag = QName(elem.tag).localname
            if elem_tag == 'Parcel':
                feature = GetterFeature().get_feature(elem, self.pg_db_connect)
                self.feature_data_list.append(feature)


class HandlerKPT10(HandlerZU):

    def __get_feature_list(self):
        self.__pg_db_connect = PgDb()
        self.context = self.etree.iterparse(self.xml, events=("end",))
        feature_name_lists = ['Parcels', 'ObjectsRealty', 'OMSPoints', 'Bounds', 'Zones']
        feature_names = ['Parcel', 'ObjectRealty', 'OMSPoint', 'SpatialData', 'Bound', 'Zone']
        for event, elem in self.context:
            elem_tag = QName(elem.tag).localname
            if elem_tag == 'CadastralBlocks':
                for child in elem.getchildren():
                    child_tag = QName(child.tag).localname
                    if child_tag == 'CadastralBlock':
                        for grandchild in child.getchildren():
                            grandchild_tag = QName(grandchild.tag).localname
                            if grandchild_tag in feature_name_lists:
                                for grandgrandchild in grandchild.getchildren():
                                    grandgrandchild_tag = QName(grandgrandchild.tag).localname
                                    if grandgrandchild_tag in feature_names:
                                        feature = GetterFeature().get_feature(grandgrandchild, self.__pg_db_connect)
                                        self.feature_data_list.append(feature)
                            elif grandchild_tag in feature_names:
                                feature = GetterFeature().get_feature(grandchild, self.__pg_db_connect)
                                self.feature_data_list.append(feature)
