from qgis.testing import start_app
from qgis.core import QgsApplication

print('setup')
app = QgsApplication([], False)

print('doing stuff with app:', app)

print('teardown')
app.exit()
del app


def foo():
    print('setup')
    app = QgsApplication([], False)

    print('doing stuff with app:', app)

    print('teardown')
    app.exit()
    del app

foo()
foo()



print('setup')
app = QgsApplication([], False)

print('doing stuff with app:', app)

print('teardown')
app.exit()
del app
