Demonstrates a few things that actually work, without causing segfaults and other bugs. 

These bugs happen because of the way Python garbage collection interacts with dependencies that are written in C++ and set up with a python API. 

To execute them, you must run them in an environment with the necessary dependencies. 

To use a build folder (ie not using an installed version of QGIS) use the setenv.sh script (which is not available in the official QGIS repo, but so far only in my own pytest branch):

    ~/wt/QGIS/pytest/build $ ./setenv.sh python ../garb/test1.py

All these four python scripts should work without issue. 
