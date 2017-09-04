# -----------------------By Kit_Angel-------------------------
# ------------------https://t.me/Kit_Angel--------------------
from lxml import etree


class CodeChecker:

    def __init__(self, etree, xml, type_xml):
        self.__etree = etree
        self.__xml = xml
        self.__type = type_xml
        self.__code = None
        self.__context = None

    def get_code(self):
        self.__context = etree.iterparse(self.__xml, events=("start-ns",))
        for event, elem in self.__context:
            self.__code = elem[1]
            break
        return self.__code

    def __del__(self):
        del self.__context


# -------------КОД-ЧЕКЕРЫ для конкретных типов--------------------

class CodeCheckerKVZU(CodeChecker):

    def __init__(self, etree, xml, type_xml):
        super().__init__(etree=etree, xml=xml, type_xml=type_xml)

    def get_code(self):
        return self.__code


