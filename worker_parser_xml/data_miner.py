"""
 обработка xml
"""
from type_and_code_checker import TypeCodeChecker
import config
from lxml import etree


class MinerData:

    def __init__(self, xml):
        self.__xml = xml
        self.__etree = etree
        self.__type_xml = None
        self.__code_xml = None
        self.__data = None

    def __get_type_and_version(self):
        type_code_checker = TypeCodeChecker(self.__etree, self.__xml)
        self.__type_xml = type_code_checker.get_type()
        self.__version_xml = type_code_checker.get_code()

    def get_data(self):
        self.__get_type_and_version()
        if self.__type_xml in config.handlers_dict.keys():
            dict_codes = config.handlers_dict[self.__type_xml]
            if self.__code_xml in dict_codes:
                get_data = dict_codes[self.__code_xml]
                self.__data = get_data(self.__etree, self.__xml, self.__code_xml)
        return self.__data


