''' create '45degreeStripes.csv' file 
    ...
'''
write = open('45degreeStripes.csv', 'w')

''' range between the 45 degree stripe signature '''
rangeBetween = 100

''' bbox of polygon '''
## type in the coordinates
yMax = 37312.3
yMin = 4382.95 

xMax = 33307.1 
xMin = 1574.08

## calculates the difference between horizontal and vertical sides of the bbox
xDif = xMax - xMin
yDif = yMax - yMin
#print "X:", xDif, "Y:", yDif

''' if x (width) longer than y (height) 
        then take xMax as end of while loop, 
    else: if y (height) longer than x (width) 
        then take xMax plus the difference of the differences
'''
if xDif >= yDif:
    xEnd = xMax
elif xDif <= yDif:
    difAddition = yDif - xDif
    xEnd = xMax + difAddition

''' while loops
    they calculates the coordinates and write it as well known text (wkt) in '45degreeStripes.csv'
'''    
## 1. from upper left corner to 'the middle' (upper right and lower left)
xMinTemp = xMin
yMaxTemp = yMax
i = 0
while xMinTemp <= xEnd:
    xMinTemp += rangeBetween
    yMaxTemp -= rangeBetween
    write.write('%s;LineString(%s %s, %s %s)\n'%(i, xMin, yMaxTemp, xMinTemp, yMax))
    i += 1
## 2. from 'the middle' to the lower right corner
xMax = xMinTemp
yMin = yMaxTemp
xMinTemp = xMin
yMaxTemp = yMax 
while xMinTemp <= xMax - (rangeBetween/2):
    xMinTemp += rangeBetween
    yMaxTemp -= rangeBetween
    write.write('%s;LineString(%s %s, %s %s)\n'%(i, xMinTemp, yMin, xMax, yMaxTemp))
    i += 1
## (2.) from the lower right to 'the middle'
#xMax = xMinTemp
#yMin = yMaxTemp
#xMaxTemp = xMinTemp
#yMinTemp = yMaxTemp    
#while xMaxTemp >= xMin + (rangeBetween/2):
    #write.write('%s;LineString(%s %s, %s %s)\n'%(i, xMaxTemp, yMin, xMax, yMinTemp))
    #xMaxTemp -= rangeBetween
    #yMinTemp += rangeBetween
    #i += 1

''' ...
    close '45degreeStripes.csv' file
'''
write.close()    

















