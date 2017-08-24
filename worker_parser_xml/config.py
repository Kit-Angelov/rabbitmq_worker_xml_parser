"""
Конфигурации для парсера
"""
from .XML_HANDLERS.xml_handlers import HandlerKVZU7
from .type_and_version_checker import CodeCheckerKVZU, CodeChecker

# списко типов
type_list = {'KPT': '...',
             'KVZU': CodeCheckerKVZU}

# словарь тип, версия : функция обработки
handlers_dict = {
    'KVZU': {"urn://x-artefacts-rosreestr-ru/outgoing/kvzu/7.0.1": HandlerKVZU7},
}

# словарь тип документа : тип сущности
type_feature = {
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

