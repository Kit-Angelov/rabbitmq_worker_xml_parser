import os
import shutil
import time
from lxml import etree
from lxml.etree import QName


class A:

    def __init__(self):
        self.dir = 'tst'

    def mk(self):
        os.mkdir(self.dir)
        print('mk Dir')
        time.sleep(7)

    def __del__(self):
        shutil.rmtree(self.dir)
        print('rm Dir')


context = etree.iterparse('example.xml', events=("start-ns", "start"))

for event, elem in context:
    if event == "start-ns":
        print(elem[1])
        break
for event, elem in context:
    if event == 'start':
        print(QName(elem.tag).localname)
        break
a = 'xml_parse_project\\worker_parser_xml\\example.xml'
print(os.path.basename(a))
print(os.path.normpath(a))
print(os.path.basename(os.path.split(a)[0]))
