import nose2
import shutil
import os
import tempfile
import pytest

from fixtures import *

from qgis.core import (
    QgsProcessingContext,
#    QgsProcessingFeedback
)
from grassprovider.grass_provider import GrassProvider
from grassprovider.grass_utils import GrassUtils


def test_neighbors(app_grass):
    app,grass = app_grass
    context = QgsProcessingContext()

    input_raster = '/home/velle/wt/QGIS/pytest/python/plugins/grassprovider/tests/testdata/float_raster.tif'
    #input_raster = os.path.join(, 'custom', 'grass7', 'float_raster.tif')

    alg = QgsApplication.processingRegistry().createAlgorithmById('grass:r.neighbors')
    assert alg is not None 

    temp_file = os.path.join('tmptest', 'grass_output.tif')

    # # Test an even integer for neighborhood size
    parameters = {'input': input_raster,
                    'selection': None,
                    'method': 0,
                    'size': 4,
                    'gauss': None,
                    'quantile': '',
                    '-c': False,
                    '-a': False,
                    'weight': '',
                    'output': temp_file,
                    'GRASS_REGION_PARAMETER': None,
                    'GRASS_REGION_CELLSIZE_PARAMETER': 0,
                    'GRASS_RASTER_FORMAT_OPT': '',
                    'GRASS_RASTER_FORMAT_META': ''}

    ok, msg = alg.checkParameterValues(parameters, context)
    assert ok is False

    print("Message:",msg)
