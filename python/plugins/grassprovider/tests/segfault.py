

import os
import yaml
import nose2
import shutil
import glob
import hashlib
import tempfile
import re

from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly
from numpy import nan_to_num
from copy import deepcopy

from qgis.core import (QgsVectorLayer,
                       QgsRasterLayer,
                       QgsCoordinateReferenceSystem,
                       QgsFeatureRequest,
                       QgsMapLayer,
                       QgsProject,
                       QgsApplication,
                       QgsProcessingContext,
                       QgsProcessingUtils,
                       QgsProcessingFeedback)
from qgis.analysis import (QgsNativeAlgorithms)
from qgis.testing import (_UnexpectedSuccess,
                          QgisTestCase,
                          start_app)

from utilities import unitTestDataPath

import processing

gdal.UseExceptions()


from grassprovider.grass_provider import GrassProvider
from grassprovider.grass_utils import GrassUtils


'''

If both start_app() and gdal.Open are called, a segfault results. 
If any of them are commented out, the segfault disappears. 

'''


class TestAlgorithmsTest(QgisTestCase):

    @classmethod
    def setUpClass(cls):
        pass
        start_app()



    def test_foo(self):
        RESULT_TIF = '/home/velle/a/QGIS/segfault.tif'
        dataset = gdal.Open(RESULT_TIF, GA_ReadOnly)
        assert False, 234


if __name__ == '__main__':
    TestAlgorithmsTest.setUpClass()
    test = TestAlgorithmsTest()
    test.test_foo()
