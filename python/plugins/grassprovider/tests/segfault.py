from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly
from qgis.testing import start_app

dataset = gdal.Open('/home/velle/a/QGIS/tests/testdata/raster/rgb_with_mask.tif', GA_ReadOnly)
start_app()
print('the end')

'''
If both of these lines are left, it gives segfault: 
 - start_app()
 - gdal.Open(...)

If any of them are commented out, the segfault disappears. 

I tried with a few different tif, and the result is the same. 

If changing the order of the two lines, some times it results in segfault, and
sometimes it results in the following fatal error:

    double free or corruption (!prev) Aborted

The print line is always executed before the fatal error occurs. 

If I modify to:

    start_app(False)

that will prevent it from calling exitQGIS(), and then there is no error. 
'''
