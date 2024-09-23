import nose2
import shutil
import os
import tempfile
import pytest

from qgis.core import (
    QgsApplication,
    QgsProcessingContext,
    QgsProcessingFeedback
)
from qgis.testing import (
    QgisTestCase,
    start_app
)
from grassprovider.grass_provider import GrassProvider
from grassprovider.grass_utils import GrassUtils

def test_grass_21():
    start_app()
    app = QgsApplication.instance()

    prvd = GrassProvider()
    app.processingRegistry().addProvider(prvd)
    print(prvd)

    prvd2 = GrassProvider()
    app.processingRegistry().addProvider(prvd2)
    print(prvd2)

    
    print(app.processingRegistry().providers())
