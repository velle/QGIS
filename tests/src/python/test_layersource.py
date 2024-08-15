import os
from qgis.testing import start_app, QgisTestCase
from utilities import unitTestDataPath
from PyQt5.QtCore import qDebug

from qgis.core import (
    QgsProject,
    QgsVectorLayer,
)

app = start_app()
TEST_DATA_DIR = unitTestDataPath()

import unittest

class TestLayerSource(QgisTestCase):
    '''
        An attempt to demonstrate a bug. I don't know if there is a better place
        to place this test, e.g. in an existing test file. For now, it gets
        its own file.
    '''

    def __init__(self, methodName):
        """Run once on class initialization."""
        QgisTestCase.__init__(self, methodName)
        self.messageCaught = False

    def testDummy(self):
        ''' Preparations/practice, before writing the actual test. '''
        qDebug( "hello world");
        prj = QgsProject.instance()
        prj.setTitle('dummy')
        self.assertFalse(False)
        p = os.path.join(TEST_DATA_DIR, 'provider', 'points.shp')
        qDebug('Does path (%s) exist? %s' % (p,os.path.exists(p)))
        layer = QgsVectorLayer(p, "layer", "ogr")

if __name__ == '__main__':
    unittest.main()
