import os
import shutil
import time
"""
from lxml import etree
from lxml.etree import QName
#, tag="{urn://x-artefacts-rosreestr-ru/outgoing/kvzu/7.0.1}Parcels"
context = etree.iterparse('examples\kpt10.xml', events=("end",))
for event, elem in context:
    if QName(elem.tag).localname == 'Parcel':
        pass
        #print(len(elem.getchildren()))

for event, elem in context:
    if QName(elem.tag).localname == 'Parcel':
        for child in elem.getchildren():
            print(QName(child.tag).localname)
            if QName(child.tag).localname == 'Name':
                print(child.text)


def get_location(elem):
    for child in elem.getchildren():
        print(child.text)

for event, elem in context:
    if QName(elem.tag).localname == 'Parcel':
        for child in elem.getchildren():
            if QName(child.tag).localname == 'Location':
                for location_child in child.getchildren():
                    if QName(location_child.tag).localname == 'Address':
                        get_location(location_child)



"""


def a():
    return '3'
