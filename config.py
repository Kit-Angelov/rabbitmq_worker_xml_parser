from worker_parser_xml.XML_HANDLERS import xml_handlers
from worker_parser_xml.code_checkers import CodeChecker

type_list = {
    'KPT': CodeChecker,
    'KVZU': CodeChecker,
    'KPZU': CodeChecker,
}

handlers_dict = {
    'KVZU': {"urn://x-artefacts-rosreestr-ru/outgoing/kvzu/7.0.1": xml_handlers.HandlerKVZU7},
    'KPZU': {"urn://x-artefacts-rosreestr-ru/outgoing/kpzu/6.0.1": xml_handlers.HandlerKPZU6},
    'KPT': {"urn://x-artefacts-rosreestr-ru/outgoing/kpt/10.0.1": xml_handlers.HandlerKPT10},
}

feature_tags = ['parcel', ]

host = 'http://192.168.2.185:8000'