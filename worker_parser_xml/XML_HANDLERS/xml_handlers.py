from lxml.etree import QName
from .BASE_HANDLER import Handler, Feature
from xml_parse_project.worker_parser_xml.XML_HANDLERS.config_handlers import type_feature


class HandlerKVZU7(Handler):

    def __init__(self, etree, xml, code_xml):
        super().__init__(etree, xml, code_xml)

    def __get_document(self):
        for event, elem in self.__context:
            if QName(elem.tag).localname == 'Date':
                if elem.text not in ['\n', '', ' ']:
                    self.document.date_formation = elem.text
            if QName(elem.tag).localname == 'Number':
                if elem.text not in ['\n', '', ' ']:
                    self.document.registration_number = elem.text

    def __get_feature_list(self):
        for event, elem in self.__context:
            if QName(elem.tag).localname == 'Parcel':
                feature = Feature()
                try:
                    parcel_data = dict(zip(elem.keys(), elem.values()))
                    feature.registration_number = parcel_data.pop('CadastralNumber')
                    feature.registration_date = parcel_data.pop('DateCreated')
                    feature.type_id = type_feature[self.__code]
                    self.feature_data_list.append(feature)
                except:
                    continue

    def __get_location(self):
        pass
