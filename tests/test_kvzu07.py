import unittest
from lxml import etree
from worker_parser_xml.type_and_code_checker import TypeCodeChecker


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