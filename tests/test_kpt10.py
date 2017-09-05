# -----------------------By Kit_Angel-------------------------
# ------------------https://t.me/Kit_Angel--------------------
import unittest
from lxml import etree
from worker_parser_xml.type_and_code_checker import TypeCodeChecker
from worker_parser_xml.XML_HANDLERS import xml_handlers


class TestKPT10(unittest.TestCase):
    def setUp(self):
        self.path_to_xml = '..\examples\kpt10_12.xml'
        self.code_xml = 'urn://x-artefacts-rosreestr-ru/outgoing/kpt/10.0.1'
        self.work_dir = ''

    def test_checked_type(self):
        type_code_checker = TypeCodeChecker(etree, self.path_to_xml)
        self.type_xml = type_code_checker.get_type()
        self.code_xml = type_code_checker.get_code()
        self.assertEqual(self.type_xml, 'KPT')
        self.assertEqual(self.code_xml, 'urn://x-artefacts-rosreestr-ru/outgoing/kpt/10.0.1')

    def test_get_data(self):
        self.getter_data = xml_handlers.HandlerKPT10(etree, self.path_to_xml, self.work_dir, self.code_xml)
        self.data = self.getter_data.get_data()


if __name__ == "__main__":
    unittest.main()
