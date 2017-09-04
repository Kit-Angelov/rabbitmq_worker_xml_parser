from shapely.geometry import Polygon
from shapely import wkt
from lxml.etree import QName


def es2wkt(elem):
    poly = None
    for child in elem.getchildren():
        if QName(child.tag).localname == 'SpatialElement':
            spatial_arr = []
            for grandchild in child.getchildren():
                if QName(grandchild.tag).localname == 'SpelementUnit':
                    for ordinate in grandchild.getchildren():
                        if QName(ordinate.tag).localname == 'Ordinate':
                            try:
                                ords = (float(ordinate.get('X')), float(ordinate.get('Y')))
                                spatial_arr.append(ords)
                            except Exception as e:
                                print(e)
                                pass
            if poly is None:
                poly = Polygon(spatial_arr)
            else:
                poly = poly.difference(spatial_arr)
    poly_wkt = wkt.dumps(poly, trim=True)
    return poly_wkt
