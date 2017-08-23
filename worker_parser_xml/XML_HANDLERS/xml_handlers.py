from lxml import etree
from lxml.etree import QName
from worker_parser_xml import config
from worker_parser_xml import base_xml_parser
from .BASE_HANDLER import BaseHandler, DocumentData, FeatureData


class KVZU7(BaseHandler):

    def __init__(self, etree, xml):
        super().__init__(etree, xml)

    def get_document_data(self):
        self.document_data = DocumentData()
        for event, elem in self.context:
            if QName(elem.tag).localname == 'Date':
                if elem.text not in ['\n', '', ' ']:
                    self.date_formation = elem.text
            if QName(elem.tag).localname == 'Number':
                if elem.text not in ['\n', '', ' ']:
                    self.registration_number = elem.text

    def get_feature_data(self):
        self.feature_data = FeatureData
        for event, elem in self.context:
            if QName(elem.tag).localname == 'Parcel':
                try:
                    parcel = []
                    parcel_data = dict(zip(elem.keys(), elem.values()))
                    parcel.append(parcel_data.pop('CadastralNumber'))
                    parcel.append(parcel_data.pop('DateCreated'))
                    self.feature_data.append(parcel)
                except:
                    continue


"""
    def xml_kvzu_parser(path_dir, file_xml):

        Обработчик файла xml типа КВЗУ
        :param path_dir: адрес архива, загружаемого пользователем
        :param file_xml: имя файла xml
        :return: возвращает данные вида:
                    {'Date': '2017-07-10',
                            'parcel_0': {'DateCreated': '2017-06-08', 'State': '06', 'CadastralNumber': '36:02:5600014:69'},
                                    'Number': '99/2017/22503527'}

        data_dict = {}
        count = 0
        context = etree.iterparse('{}/{}'.format(path_dir, file_xml), events=("end",))
        for event, elem in context:
            if QName(elem.tag).localname == 'Parcel':
                try:
                    parcel_data = dict(zip(elem.keys(), elem.values()))
                    parcel_data['registration_number'] = parcel_data.pop('CadastralNumber')
                    parcel_data['registration_date'] = parcel_data.pop('DateCreated')
                    data_dict['parcel_{}'.format(str(count))] = parcel_data
                    print(parcel_data)
                    count += 1
                except:
                    continue
            if QName(elem.tag).localname == 'Date':
                if elem.text not in ['\n', '', ' ']:
                    data_dict['date_formation'] = elem.text
                    print(elem.text)

            if QName(elem.tag).localname == 'Organization':
                if elem.text not in ['\n', '', ' ']:
                    data_dict['Organization'] = elem.text
                    print(elem.text)
            if QName(elem.tag).localname == 'Number':
                if elem.text not in ['\n', '', ' ']:
                    data_dict['registration_number'] = elem.text
                    print(elem.text)
            elem.clear()
        print(data_dict)
        del context
        return data_dict


if __name__ == '__main__':
    xml_kvzu_parser('dirs/parse', '36 02 5600014 69 10-07-2017.xml')
"""