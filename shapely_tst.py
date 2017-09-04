import shapely
from shapely.geometry import Polygon
from shapely import wkt
"""
hole = Polygon(((1, 1), (1, 2), (2, 2)))
hole2 = Polygon(((3, 3), (3, 4), (4, 4)))
poly = Polygon(((0, 0), (0, 6), (6, 6), (6, 0)))
res_poly = Polygon([(0, 0), (0, 6), (6, 6), (6, 0)], [((1, 1), (1, 2), (2, 2)), ((3, 3), (3, 4), (4, 4))])
print(poly.area)
new_poly = poly.difference(hole)
new_new_poly = new_poly.difference(hole2)
print(poly.wkt)
print(new_poly.wkt)
print(new_poly.area)
print(new_new_poly.area)
print(new_new_poly.wkt)
print(res_poly.area)
print(res_poly.wkt)
"""
from lxml import etree
from lxml.etree import QName

context = etree.iterparse('examples\kvzu07.xml', events=("end",))
for event, elem in context:
    if QName(elem.tag).localname == 'SpatialElement':
        ords_arr = []
        for child in elem.getchildren():
            if QName(child.tag).localname == 'SpelementUnit':
                for ordinate in child.getchildren():
                    if QName(ordinate.tag).localname == 'Ordinate':
                        try:
                            ords = (float(ordinate.get('X')), float(ordinate.get('Y')))
                            ords_arr.append(ords)
                            print(ordinate.get('X'))
                            print(ordinate.get('Y'))
                        except Exception as e:
                            print(e)
                            pass
        print(ords_arr)
        poly = Polygon(ords_arr)
        print(poly.area)
        poly_wkt = wkt.dumps(poly, trim=True)
        print(poly_wkt)
        print(type(poly.wkt))

po = Polygon([])
print(po)




