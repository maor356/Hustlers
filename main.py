# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:33:06 2018

@author: Rens
"""
try: import pylab
except ImportError: pylab_installed = False
else: pylab_installed = True
from random import randint
import copy

class Tile:
    
    x = None
    y = None
    sideWays = False
    def __init__(self,width,height):
        self.width= int(width)
        self.height = int(height)
        
        
def checkLeftCorner(x,y,width,height):
    
    if (int(x)+int(width) > widthField) or (int(x) < 0) or ((int(y)+int(height) > heightField) or (int(y)) < 0):
        
        return False
    for i in range(int(x),int(x)+int(width)):
        for j in range(int(y),int(y)+int(height)):
           
            if(coordinateList[i][j] == 1):
                return False
    
    return True
def paintField(field,x,y,width,height):  
    
    for i in range(x,x+width):
        for j in range(y,y+height):
            
            field[i][j] = 1
    
def sum2darray(input):
    return sum(map(sum, input))


file = open("C:/Users/Rens2/Documents/simple.tiles","r") 
tileList = []


properties = file.readline().rstrip().split(" ")
widthField = int(properties[1])
heightField = int(properties[3])
scaleField = int(properties[5])

coordinateList = [[0 for x in range(heightField)] for y in range(widthField)] 

for line in file: 
    tileCount = int(line.split(" ")[0])
    widthAndHeight = line.split(" ")[2].split("x")
    width = widthAndHeight[0]
    height = widthAndHeight[1]
    
    for i in range(tileCount):       
        tileList.append(Tile(width,height))
        

  
#random placement algorithm
usedTiles = []
unusedTiles = copy.deepcopy(tileList)
notSolved = True
placeable = True
freshCoordinates = copy.deepcopy(coordinateList)
maxReached = 0
while (notSolved):
    
            
    usedTiles = []
    unusedTiles = copy.deepcopy(tileList)
    unusedCoordinates = copy.deepcopy(freshCoordinates)
    coordinateList = copy.deepcopy(freshCoordinates)
    placeable = True
    
    while(len(unusedTiles) > 0 and placeable == True):
        nextTile = unusedTiles.pop(randint(0,len(unusedTiles)-1))
        
        placed = False
       
        
        while (sum2darray(unusedCoordinates) < widthField*heightField) and (placed == False):
            randX = randint(0,widthField-1)
            randY = randint(0,heightField-1)
            
            if (unusedCoordinates[randX][randY] == 0):
                
                if (checkLeftCorner(randX,randY,nextTile.width,nextTile.height) == True):
                    nextTile.x = randX
                    nextTile.y = randY
                    paintField(coordinateList,randX,randY,nextTile.width,nextTile.height)
                    usedTiles.append(nextTile)
                    placed = True
                elif (checkLeftCorner(randX,randY,nextTile.height,nextTile.width) == True):
                    nextTile.x = randX
                    nextTile.y = randY
                    nextTile.sideWays = True
                    paintField(coordinateList,randX,randY,nextTile.height,nextTile.width)
                    usedTiles.append(nextTile)
                    placed = True
                else:
                    unusedCoordinates[randX][randY] = 1
                  
        if (placed == False):
            placeable = False

 
    
    if (len(unusedTiles) == 0) and (placeable == True):
        notSolved = False
        
for i in range(len(usedTiles)):       
        print(usedTiles[i].x,",",usedTiles[i].y,",",usedTiles[i].width,",",usedTiles[i].height,",",usedTiles[i].sideWays)
        
    
if pylab_installed:
    pylab.axis([0, widthField, 0, heightField])
    pylab.grid()
    pylab.xticks(range(widthField+1))
    pylab.yticks(range(heightField+1))
   
    pylab.show()