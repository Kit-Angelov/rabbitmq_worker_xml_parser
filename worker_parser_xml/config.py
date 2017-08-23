"""
Конфигурации для парсера
"""
from worker_parser_xml.XML_HANDLERS.XML_KVZU_7 import xml_kvzu_parser
from .type_and_version_checker import VersionCheckerKVZU
from .XML_HANDLERS.xml_handlers import KVZU7

# списко типов
type_list = {'KPT': '...',
             'KVZU': VersionCheckerKVZU}

# словарь тип, версия : функция обработки
handlers_dict = {
    'KVZU': {'7': KVZU7},
}

# словарь тип документа : тип сущности
type_feature_dict = {
    'КВЗУ': 'ЗУ',
}

# список названий в xml типов feature
feature_tags = ['parcel', ]

# путь до бд sqlite
sqlite_params = '..\\rabbit\db.sqlite3'

# параметры подключения к бд PG
pg_params = {
            'database': "rrd",              # database_name
            'user': "postgres",             # user_name
            'password': "root",             # password
            'host': "192.168.2.252",        # host
            'port': "5432"                  # port
}

