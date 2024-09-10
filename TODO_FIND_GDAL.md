STATUS UPDATE, SEP 10: It kind of works, but after choosing GDAL_SEARCH_MODE=MODULE, one must configure twice before variables such as GDAL_LIBRARY are displayed. 

ISSUE: It is possible that this has nothing to do with my code, and instead it has to do with the implementation of the legacy finder. 

TODO: One simple improvement would be to change the GDAL_SEARCH_MODE variable so it can only be one of the three fixed values, MODULE, CONFIG, or CONFIG_THEN_MODULE. 

TODO: There should be some documentation on this somewhere, and the "help text" for GDAL_SEARCH_MODE should have a URL that points to this. 




TODO: I need to find the place, where it said that GDAL_DIR was the same as configure prefix. It's not. 

TODO: Find place, where they suggest both GDAL_DIR and GDAL_ROOT. Remove GDAL_ROOT, or at least make it clear that they do exactly the same; if they do. 


LEARN: Which variables need to be set by cmake config. Maybe the config search actually also sets GDAL_LIBRARY and GDAL_INCLUDE_DIR, and these are the most important, maybe the only important? Maybe they are set, but declared 'internal'. No, I don't think so, because they are not set in CMakeCache.txt. 

INVESTIGATE: Look into the default FindGDAL.cmake that comes with cmake. It is not necessarily available on all platforms, e.g. not available on Ubuntu 22.04. But it might be more correct, or it might provide inspiration for how to do it more elegantly. Maybe that module combines a search algorithm and config search. 

INVESTIGATE: What's with proj. Does it have the exact same issue? It prints something similar to the terminal. 

BETTER SOLUTION ? ? ? 

I don't think the current solution is elegant. And I think there must be other ways of doing it. 

It would be simple to make a solution that first uses config mode, then module mode, or conversely, first uses module mode, then config mode. 
But it's not easy to make a solution that will then still allow the user to choose the secondary if the primary finds a candidate. That's what I tried to build. 


