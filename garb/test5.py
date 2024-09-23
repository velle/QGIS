from qgis.core import QgsApplication

def get_app():
    print('setup')
    app = QgsApplication([], False)
    QgsApplication.instance()
    return app

app = get_app()
print('doing stuff with app:', app)
print('teardown')
del app


app = get_app()
print('doing stuff with app:', app)
print('teardown')
del app


app = get_app()
print('doing stuff with app:', app)
print('teardown')
del app

