"""
 обработка xml
"""
from .type_and_version_checker import TypeVersionChecker
import os
from . import config
from lxml import etree


class MinerData:

    def __init__(self, xml):
        self.__xml = xml
        self.__etree = etree
        self.__type_xml = None
        self.__code_xml = None
        self.__data = None

    def __get_type_and_version(self):
        type_version_checker = TypeVersionChecker(self.__etree)
        self.__type_xml = type_version_checker.get_type(self.__xml)
        self.__version_xml = type_version_checker.get_code(self.__xml, self.__type_xml)

    def get_data(self):
        self.__get_type_and_version()
        if self.__type_xml in config.handlers_dict.keys():
            dict_codes = config.handlers_dict[self.__type_xml]
            if self.__code_xml in dict_codes:
                get_data = dict_codes[self.__code_xml]
                self.__data = get_data(self.__etree, self.__xml, self.__code_xml)
        return self.__data


