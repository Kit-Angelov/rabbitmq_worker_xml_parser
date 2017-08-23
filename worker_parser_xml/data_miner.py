"""
 обработка xml
"""

from worker_parser_xml import config
from worker_parser_xml.type_parser import check_type_and_version
import cyrtranslit
from lxml import etree


# выбор обработчика xml по типу и версии
def select_handler(type_xml, version):
    """
    Выбор определенного обработчика из XML_HANDLERS для определенного типа документа
    :param type_xml: тип документа
    :param version: версия документа
    :return: функция обработки документа
    """
    handler = ','.join((type_xml, version))
    return config.handlers_dict[handler]


# главный метод данного пакета - узнает тип документа, обрабатывает, получает данные и потправляет их в loader
def parser_xml(path_zip):
    """
    главная функция обработки документа
    :param path_zip: адрес архива, загружаемого пользователем
    :return: возвращает данные вида:
    {'parcel_0': {'State': '06', 'DateCreated': '2017-06-08', 'CadastralNumber': '36:02:5600014:69'},
     'Date': '2017-07-10',
      'Number': '99/2017/22503527',
       'type': 'КВЗУ',
       'version': '7'}
    """
    type_ver_dict, path_dir, file_xml = check_type_and_version(path_zip)

    type_xml = type_ver_dict[file_xml]['type']
    version = type_ver_dict[file_xml]['version']

    type_cyr = cyrtranslit.to_cyrillic(type_xml)

    func = select_handler(type_xml, version)
    data = func(path_dir, file_xml)
    data['type'] = type_cyr
    data['version'] = version
    return data


if __name__ == '__main__':
    print(parser_xml('zips/parse.zip'))


from .type_and_version_checker import TypeVersionChecker
import os
from . import config
from lxml import etree


class DocumentData:

    def __init__(self):
        self.date_formation = None
        self.registration_number = None


class FeatureData:

    def __init__(self):
        self.registration_number = None
        self.registration_date = None


class DataMiner:

    def __init__(self):
        self.__xml = None
        self.__etree = etree
        self.__data = None
        self.__type_xml = None
        self.__version_xml = None

    def __get_type_and_version(self, xml):
        self.__xml = xml
        type_version_checker = TypeVersionChecker(self.__etree)
        self.__type_xml = type_version_checker.get_type(self.__xml)
        self.__version_xml = type_version_checker.get_version(self.__xml, self.__type_xml)

    def get_data(self):
        if self.__type_xml in config.handlers_dict.keys():
            dict_versions = config.handlers_dict[self.__type_xml]
            if self.__version_xml in dict_versions:
                handler_xml_class = dict_versions[self.__version_xml]
                handler_xml = handler_xml_class(self.__etree, self.__xml)


        pass
