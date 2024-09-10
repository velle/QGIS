STATUS UPDATE, SEP 10: It kind of works, but after choosing GDAL_SEARCH_MODE=MODULE, one must configure twice before variables such as GDAL_LIBRARY are displayed. 

## ISSUE: 
It is possible that this has nothing to do with my code, and instead it has to do with the implementation of the legacy finder. 

## TODO: 
One simple improvement would be to change the GDAL_SEARCH_MODE variable so it can only be one of the three fixed values, MODULE, CONFIG, or CONFIG_THEN_MODULE. 

## TODO: 
There should be some documentation on this somewhere, and the "help text" for GDAL_SEARCH_MODE should have a URL that points to this. 




## TODO: 
I need to find the place, where it said that GDAL_DIR was the same as configure prefix. It's not. 

## TODO: 
Find place, where they suggest both GDAL_DIR and GDAL_ROOT. Remove GDAL_ROOT, or at least make it clear that they do exactly the same; if they do. 


## LEARN: 
Which variables need to be set by cmake config. Maybe the config search actually also sets GDAL_LIBRARY and GDAL_INCLUDE_DIR, and these are the most important, maybe the only important? Maybe they are set, but declared 'internal'. No, I don't think so, because they are not set in CMakeCache.txt. 

## INVESTIGATE: 
Look into the default FindGDAL.cmake that comes with cmake. It is not necessarily available on all platforms, e.g. not available on Ubuntu 22.04. But it might be more correct, or it might provide inspiration for how to do it more elegantly. Maybe that module combines a search algorithm and config search. 

## INVESTIGATE: 
What's with proj. Does it have the exact same issue? It prints something similar to the terminal. 

## TODO:

Check which variables are actually set by FindGDAL.cmake. The version that comes with cmake/Ubuntu is documented here: https://cmake.org/cmake/help/latest/module/FindGDAL.html. Then test if I'm unsetting too many variables. 

## LEARN: What is an imported target

See: https://cmake.org/cmake/help/latest/module/FindGDAL.html. 

# What would be a better solution?

I don't think the current solution is elegant. And I think there must be other ways of doing it. 

It would be simple to make a solution that first uses config mode, then module mode, or conversely, first uses module mode, then config mode. 
But it's not easy to make a solution that will then still allow the user to choose the secondary if the primary finds a candidate. That's what I tried to build. 

When 


# LEARN: Is the cmake/Ubuntu version FindGDAL.cmake only for Ubuntu

CMake is a tool used on many platforms. When I install cmake with apt on Ubuntu, maybe the cmake modules are different, vs if I install cmake on Windows or Mac. Maybe Ubuntu maintains some of the cmake files, such that even for a specific verion, e.g. cmake 3.22, FindGDAL.cmake will look different on Fedora and Ubuntu. 

Maybe those cmake files are independent of the cmake version. Ie upgrading cmake will not upgrade FindGDAL.cmake. 


# How cmake made their FindGDAL.cmake

The following is from the FindGDAL.cmake that comes with cmake on Ubuntu 22.04. 

    /usr/share/cmake-3.22/Modules/FindGDAL.cmake

> The following variables may be set to modify the search strategy:
> 
> ``FindGDAL_SKIP_GDAL_CONFIG``
>   If Version <YY> of the package was found if true. Authors of find modules should make sure at most one of these is ever true. For example TCL_VERSION_84.

set, ``gdal-config`` will not be used. This can be useful if there are
>   GDAL libraries built with autotools (which provide the tool) and CMake (which
>   do not) in the same environment.
> ``GDAL_ADDITIONAL_LIBRARY_VERSIONS``
>   Extra versions of library names to search for.

It is not possible to chose this from ccmake alone. One must know how to specify FindGDAL_SKIP_GDAL_CONFIG from command line. 

Is that good enough? Maybe. It would be great if, if it was easier to find, ie find the docs that instruct to set this variable. 



# LEARN: Calling local version of module

E.g. the QGIS version of FindGDAL.cmake could (when certain conditions are met) call the local Ubuntu-distributed version of FindGDAL.cmake. The only way I found that can do this is hacky. Which suggests that this is not generally used and not best practice. But why? And what should I do instead.

# ASK: How to use gdal < 3.5 in an environment with GDAL >= 3.5

I don't think its possible with the current QGIS version of FindGDAL.cmake.  

If deleting the QGIS version of FindGDAL.cmake, it will then use the Ubuntu version instead. This cmake file starts with the old school process (aka module search) which btw uses a CLI tool called `gdal-config`. 

AFAIU this tool is legacy and is only generated when running `autotools`, not when running cmake. 

To force it to not use gdal-configure, one can set FindGDAL_SKIP_GDAL_CONFIG. I'm guessing this corresponds much to 

# ASK: Naming convention for FindGDAL_SKIP_GDAL_CONFIG

I would have ensured it started with `GDAL_`. But perhaps its a convention to prefix with `FindGDAL`. 

This is relevant if I decide to use the same variable in the QGIS version of FindGDAL.cmake. 

# Convention: GDAL_DIR points to folder with CMake files

Det sker helt automatisk med config search. Læs bl.a. her https://cmake.org/cmake/help/v3.30/command/find_package.html:

> Config mode attempts to locate a configuration file provided by the package to be found. A cache entry called <package>_DIR is created to hold the directory containing the file. 

But the (soon to be legacy) QGIS-shipped FindGDAL.cmake uses GDALDIR/GDAL_DIR/GDAL_ROOT to refer to the install prefix. 

Docs seem to suggest that they should use GDAL_ROOT_DIR instead. 

Der er en lille stump kode i QGIS FindGDAL.cmake, hvor de bruger GDAL_PREFIX, men jeg kan ikke se, hvor det bliver defineret. 
