from lxml import etree


class DocumentData:

    def __init__(self):
        self.date_formation = None
        self.registration_number = None


class FeatureData:

    def __init__(self):
        self.registration_number = None
        self.registration_date = None



class BaseHandler:

    def __init__(self, etree, xml):
        self.document_data = None
        self.feature_data_list = []
        self.feature_data = None
        self.__etree = etree
        self.__xml = xml
        self.context = self.__etree.iterparse(self.__xml, events=("end",))

    def get_document_data(self):
        pass

    def get_feature_data(self):
        pass

