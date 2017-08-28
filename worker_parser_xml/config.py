from xml_parse_project.worker_parser_xml.XML_HANDLERS.xml_handlers import HandlerKVZU7

from xml_parse_project.worker_parser_xml.type_and_code_checker import CodeChecker

type_list = {'KPT': '...',
             'KVZU': CodeChecker}

handlers_dict = {
    'KVZU': {"urn://x-artefacts-rosreestr-ru/outgoing/kvzu/7.0.1": HandlerKVZU7},
}

feature_tags = ['parcel', ]