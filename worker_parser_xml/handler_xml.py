"""
 обработка xml
"""

from worker_parser_xml import config
from worker_parser_xml.type_parser import check_type_and_version
import cyrtranslit


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
