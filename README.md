## 45°-polygon-signature workaround solution
creates a 45° signature for polygons 
[for map viewer with no support of polygon signatures (e.g. with raster formats like *.png)]

1. get upper left and lower right corner coordinates of polygon bounding box
 -- QuantumGIS -> right click on layer -> `Properties -> Properties>>Extents`

2. type in the coordinates in the python script 
 -- start the python script: `~$ python 45degreeStripes.py`
 -- the output is an CSV file with linestrings in the well known text format; something like: 
```0; LineString(x y, x y)  
1; LineString(x y, x y)  
...
```

3. open 45degreeStripes.csv in quantum GIS  

4. clip 45° stripes with polygon
 -- `Vector -> Geoprocessing Tools -> Clip`

5. fin 

