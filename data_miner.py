"""
 обработка xml
"""
import type_and_code_checker
import config
from lxml import etree
import os


class MinerData:

    def __init__(self, xml, work_dir):
        self.__work_dir = work_dir
        self.__xml = os.path.join(self.__work_dir, xml)
        self.__etree = etree
        self.__type_xml = None
        self.__code_xml = None
        self.__data = None

    def __get_type_and_version(self):
        type_code_checker = type_and_code_checker.TypeCodeChecker(self.__etree, self.__xml)
        self.__type_xml = type_code_checker.get_type()
        self.__code_xml = type_code_checker.get_code()
        print('Type xml: {}'.format(self.__type_xml))
        print('Code xml: {}'.format(self.__code_xml))

    def get_data(self):
        self.__get_type_and_version()
        if self.__type_xml in config.handlers_dict.keys():
            dict_codes = config.handlers_dict[self.__type_xml]
            if self.__code_xml in dict_codes:
                getter_data = dict_codes[self.__code_xml]
                print('Getter of data: {}'.format(getter_data.__name__))
                self.__data = getter_data(self.__etree, self.__xml, self.__work_dir, self.__code_xml)
                self.__data.get_data()
        return self.__data


