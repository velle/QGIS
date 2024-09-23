import pytest
from qgis.testing import start_app
from qgis.core import QgsApplication
from grassprovider.grass_provider import GrassProvider


@pytest.fixture(scope='function')
def app():
    print('setup')
    app = QgsApplication([], False)
    return app


@pytest.fixture(scope='function')
def app_td():
    '''
    _td: with tear down

    This is supposedly the correct way for adding a teardown phase to a fixture in pytest.
    By using `yield`. But I can't make it work. 
    '''
    print('setup')
    app = QgsApplication([], False)
    
    yield app

    print('teardown 1')
    app.exitQgis()
    print('teardown 2')
    del app
    print('teardown 3')


@pytest.fixture(scope='function')
def app_grass():
    print('setup')

    # Does not work when I instantiate like this (constructor and init). 
    # Causes segfault. Why must I use start_app()?

    # app = QgsApplication([],False)
    # app.init()

    start_app(False)
    app = QgsApplication.instance()

    prvd = GrassProvider()
    app.processingRegistry().addProvider(prvd)

    return app, prvd
