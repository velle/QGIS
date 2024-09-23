from qgis.testing import start_app
from qgis.core import QgsApplication

# Iteration 1

print('setup')
app = QgsApplication([], False)

print('doing stuff with app:', app)

print('teardown')
app.exit()
del app


# Iteration 2

print('setup')
app = QgsApplication([], False)

print('doing stuff with app:', app)

print('teardown')
app.exit()
del app
