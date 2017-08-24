from lxml import etree
from worker_parser_xml import config
from worker_parser_xml.base_functions import mk_temp_dir, rm_temp_dir, unzip


# проверка типа документа
def check_type_and_version(path_zip):
    """
    Проверка типа и версии документа
    :param path_zip: адрес архива, загружаемого пользователем
    :return: словарь : тип документа и версия, путь к "временной" директории , имя файла xml
    """
    files, path_dir = unzip(path_zip)
    print(files, path_dir)
    file_xml = ''
    type_ver_dict = {}
    try:
        for file in files:
            if str(file).endswith('.xml'):
                file_xml = str(file)
                break
    except:
        file_xml = str(files)
    print(file_xml)
    context = etree.iterparse(path_dir + '/' + file_xml, events=("start",))
    for event, elem in context:
        if elem.tag.split('}')[1] in config.type_list:
            version, type = elem.tag.split('}')
            print(elem.tag)
            version = version.replace('{', '').split('/')[-1].split('.')[0]
            print('type: ', type, '\nversion: ', version)

            type_ver_dict[str(file_xml)] = {'type': type, 'version': version}
            break
        elem.clear()
    del context

    #print(tree.getroot().tag)
    #version, type = tree.getroot().tag.split('}')

    print(type_ver_dict)
    #rm_temp_dir(path_dir)
    return type_ver_dict, path_dir, file_xml


if __name__ == '__main__':
    check_type_and_version('parse.zip')


from . import config


class TypeVersionChecker:

    def __init__(self, etree):
        self.__etree = etree
        self.__xml = None
        self.__type = None
        self.__code = None

    def get_type(self, xml):
        self.__xml = xml
        return self.__type

    def get_code(self, xml, type_xml):
        self.__xml = xml
        self.__type = type_xml
        if self.__type in config.type_list.keys():
            code_checker_class = config.type_list[self.__type]
            code_checker = code_checker_class(self.__etree, self.__xml, self.__type)
            self.__code = code_checker.get_code()
        return self.__code


class CodeChecker:

    def __init__(self, etree, xml, type_xml):
        self.__etree = etree
        self.__xml = xml
        self.__type = type_xml
        self.code = None

    def get_code(self):
        pass


class CodeCheckerKVZU(CodeChecker):

    def __init__(self, etree, xml, type_xml):
        super().__init__(etree=etree, xml=xml, type_xml=type_xml)

    def get_code(self):
        return self.code
