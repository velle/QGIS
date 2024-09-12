from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly
from qgis.testing import start_app

'''
If both of these lines are left, it gives segfault: 
 - start_app()
 - gdal.Open are called

If any of them are commented out, the segfault disappears. 

Changing the order of them still causes segfault
'''

if __name__ == '__main__':
    start_app()
    dataset = gdal.Open('/home/velle/a/QGIS/tests/testdata/raster/rgb_with_mask.tif', GA_ReadOnly)
