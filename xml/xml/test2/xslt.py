# -----------------------By Kit_Angel-------------------------
# ------------------https://t.me/Kit_Angel--------------------
from lxml import etree

path_xml = 'test2.xml'
path_xslt = 'test2.xsl'

transform = etree.XSLT((etree.parse(path_xslt)))
source = etree.parse(path_xml)
result = etree.tostring(transform(source))

with open('res.html', 'wb') as res:
    res.write(result)
print(result)


