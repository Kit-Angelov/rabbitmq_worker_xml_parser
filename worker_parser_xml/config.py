from xml_parse_project.worker_parser_xml.XML_HANDLERS.xml_handlers import HandlerKVZU7, HandlerKPZU6, HandlerKPT10

from xml_parse_project.worker_parser_xml.type_and_code_checker import CodeChecker

type_list = {
    'KPT': CodeChecker,
    'KVZU': CodeChecker,
    'KPZU': CodeChecker,
}

handlers_dict = {
    'KVZU': {"urn://x-artefacts-rosreestr-ru/outgoing/kvzu/7.0.1": HandlerKVZU7},
    'KPZU': {"urn://x-artefacts-rosreestr-ru/outgoing/kpzu/6.0.1": HandlerKPZU6},
    'KPT': {"urn://x-artefacts-rosreestr-ru/outgoing/kpt/10.0.1": HandlerKPT10},
}

feature_tags = ['parcel', ]
