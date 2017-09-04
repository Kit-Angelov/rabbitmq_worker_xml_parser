from lxml.etree import QName
from worker_parser_xml.XML_HANDLERS import BASE_HANDLER


def get_document(obj):
    obj.context = obj.etree.iterparse(obj.xml, events=("end",))
    for event, elem in obj.context:
        if QName(elem.tag).localname == 'CertificationDoc':
            for child in elem.getchildren():
                if QName(child.tag).localname == 'Date':
                    if child.text not in ['\n', '', ' ']:
                        obj.document.date_formation = child.text
                        print('Document date formation: {}'.format(obj.document.date_formation))
                if QName(child.tag).localname == 'Number':
                    if child.text not in ['\n', '', ' ']:
                        obj.document.registration_number = child.text
                        print('Document registration number: {}'.format(obj.document.registration_number))


def get_location(feature, elem):
    for child in elem.getchildren():
        if QName(child.tag).localname == 'OKATO':
            feature.location.okato = child.text
            print('Location okato: {}'.format(feature.location.oktmo))
        if QName(child.tag).localname == 'KLADR':
            feature.location.kladr = child.text
            print('Location kladr: {}'.format(feature.location.oktmo))
        if QName(child.tag).localname == 'Note':
            feature.location.note = child.text
            print('Location note: {}'.format(feature.location.oktmo))
        if QName(child.tag).localname == 'Region':
            feature.location.region = child.text
            print('Location region: {}'.format(feature.location.oktmo))
        else:
            try:
                feature.location.note == elem.text
                print('Location note: {}'.format(feature.location.oktmo))
            except Exception as e:
                print('Error: ', e)
                pass


class GetterFeature:

    def __init__(self):
        self.feature = BASE_HANDLER.Feature()

    def get_feature(self, elem, pg_db_connection):
        func_dict = {
            'Parcel': self.__get_feature_parcel,
            'ObjectRealty': self.__get_feature_object_realty,
            'OMSPoint': self.__get_feature_oms_point,
            'SpatialData': self.__get_feature_spatial_data,
            'Bound': self.__get_feature_bound,
            'Zone': self.__get_feature_zone
        }
        tag = QName(elem.tag).localname
        try:
            func = func_dict[str(tag)]
            self.feature = func(elem)
            self.feature.type_id = pg_db_connection.get_feature_type_id(self.feature.code)
            print('Feature type id: {}'.format(self.feature.type_id))
            return self.feature
        except Exception as e:
            print('Error: ', e)

    def __get_feature_parcel(self, elem):
        self.feature.code = 'Parcel'
        print('Feature code: {}'.format(self.feature.code))
        for child in elem.getchildren():
            if QName(child.tag).localname == 'Location':
                for location_child in child.getchildren():
                    if QName(location_child.tag).localname == 'Address':
                        get_location(self.feature, location_child)
        try:
            parcel_data = dict(zip(elem.keys(), elem.values()))
            self.feature.registration_number = parcel_data.pop('CadastralNumber')
            print('Feature registration number: {}'.format(self.feature.registration_number))
            self.feature.registration_date = parcel_data.pop('DateCreated')
            print('Feature registration date: {}'.format(self.feature.registration_date))
        except Exception as e:
            print('Error: ', e)
            pass
        return self.feature

    def __get_feature_object_realty(self, elem_parent):
        elem = elem_parent.getchildren()[0]
        self.feature.code = 'OKS_{0}'.format(QName(elem.tag).localname)
        print('Feature code: {}'.format(self.feature.code))
        for child in elem.getchildren():
            if QName(child.tag).localname == 'Address':
                get_location(self.feature, child)
        try:
            parcel_data = dict(zip(elem.keys(), elem.values()))
            self.feature.registration_number = parcel_data.pop('CadastralNumber')
            print('Feature registration number: {}'.format(self.feature.registration_number))
        except Exception as e:
            print('Error: ', e)
            pass
        return self.feature

    def __get_feature_oms_point(self, elem):
        self.feature.code = 'OMS'
        print('Feature code: {}'.format(self.feature.code))
        reg_numb_dict = {'PKlass': '', 'PName': '', 'PNmb': ''}
        for child in elem.getchildren():
            if QName(child.tag).localname in reg_numb_dict:
                reg_numb_dict[QName(child.tag).localname] = child.text
        self.feature.registration_number = '{0} {1} {2}'.format(reg_numb_dict['PKlass'],
                                                                reg_numb_dict['PName'],
                                                                reg_numb_dict['PNmb'])
        print('Feature registration number: {}'.format(self.feature.registration_number))
        return self.feature

    def __get_feature_spatial_data(self, elem):
        self.feature.code = 'Kvartal'
        print('Feature code: {}'.format(self.feature.code))
        try:
            parcel_data = dict(zip(elem.keys(), elem.values()))
            self.feature.registration_number = parcel_data.pop('CadastralNumber')
            print('Feature registration number: {}'.format(self.feature.registration_number))
        except Exception as e:
            print('Error: ', e)
            pass
        return self.feature

    def __get_feature_bound(self, elem):
        code_dict = {
            'SubjectsBoundary': (lambda: 'Bound_{0}'.format(QName(child.tag).localname))(),
            'MunicipalBoundary': (lambda: 'Bound_{0}'.format(QName(child.tag).localname))(),
            'InhabitedLocalityBoundary': (lambda: 'Bound_{0}'.format(QName(child.tag).localname))(),
        }
        for child in elem.getchildren():
            if QName(child.tag).localname in code_dict.keys():
                self.feature.code = (code_dict[QName(child.tag).localname])
                print('Feature code: {}'.format(self.feature.code))
            if QName(child.tag).localname == 'AccountNumber':
                self.feature.registration_number = child.text
                print('Feature registration number: {}'.format(self.feature.registration_number))
            if QName(child.tag).localname == 'Description':
                get_location(self.feature, child)
        return self.feature

    def __get_feature_zone(self, elem):
        code_dict = {
            'TerritorialZone': (lambda: 'Zone_{0}'.format(QName(child.tag).localname))(),
            'SpecialZone': (lambda: 'Zone_{0}'.format(QName(child.tag).localname))(),
        }
        for child in elem.getchildren():
            if QName(child.tag).localname in code_dict.keys():
                self.feature.code = (code_dict[QName(child.tag).localname])
                print('Feature code: {}'.format(self.feature.code))
            if QName(child.tag).localname == 'AccountNumber':
                self.feature.registration_number = child.text
                print('Feature registration number: {}'.format(self.feature.registration_number))
            if QName(child.tag).localname == 'Description':
                get_location(self.feature, child)
        return self.feature
