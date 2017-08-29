import os
import shutil
import time
from lxml import etree
from lxml.etree import QName


class A:

    def first(self):
        a = 2
        b = 4
        return a+b

class B(A):
    pass

c = B()
print(c.first())
