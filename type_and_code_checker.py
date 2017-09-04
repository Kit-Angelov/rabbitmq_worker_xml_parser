from lxml import etree
from lxml.etree import QName
from worker_parser_xml import config
import unittest


class TypeCodeChecker:

    def __init__(self, etree, xml):
        self.__etree = etree
        self.__xml = xml
        self.__type = None
        self.__code = None
        self.__context = None

    def get_type(self):
        self.__context = etree.iterparse(self.__xml, events=("start",))
        for event, elem in self.__context:
            self.__type = QName(elem.tag).localname
            break
        return self.__type

    def get_code(self):
        if self.__type in config.type_list.keys():
            code_checker_class = config.type_list[self.__type]
            code_checker = code_checker_class(self.__etree, self.__xml, self.__type)
            self.__code = code_checker.get_code()
        return self.__code

    def __del__(self):
        del self.__context


# --------------TESTs-------------------


class TestKVZU07(unittest.TestCase):
    def setUp(self):
        self.path_to_xml = 'examples\kvzu07.xml'

    def test_checked_type(self):
        type_code_checker = TypeCodeChecker(etree, self.path_to_xml)
        self.type_xml = type_code_checker.get_type()
        self.code_xml = type_code_checker.get_code()
        self.assertEqual(self.type_xml, 'KVZU')
        self.assertEqual(self.code_xml, 'urn://x-artefacts-rosreestr-ru/outgoing/kvzu/7.0.1')

if __name__ == "__main__":
    unittest.main()