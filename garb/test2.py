from qgis.core import QgsApplication

def foo():
    print('setup')
    app = QgsApplication([], False)

    print('doing stuff with app:', app)

    print('teardown')
    app.exit()
    del app

foo()
foo()