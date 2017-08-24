import os
import shutil
import time


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

