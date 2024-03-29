# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:13:42 2018

@author: Rens
"""
import time
import copy
import os
import math
from colored import fg,bg, attr

class Tile:
    def __init__(self,width,height, tilenumber):
        self.width= int(width)
        self.height = int(height)
        self.tilenumber = int(tilenumber)

def printField(field):
    for x in range(len(field[0])):
        print("%s%3s" % (attr("reset"),"-"),end="")
    print("")
    for y in range(len(field)):
        print("%s|" % attr("reset"), end = ""),
        for x in range(len(field[y])):
            if (x == (len(field[y]) - 1)):
                    print('%s%s%2d%s|' % (bg(field[y][x]),fg(field[y][x]+3),field[y][x],attr("reset")), end = "")
            else:
                print('%s%s%2d|' % (bg(field[y][x]),fg(field[y][x]+3),field[y][x]), end = "")
        print("\n%s" % (fg('black')), end="")
    for x in range(len(field[0])):
         print("%s%3s" % (attr("reset"),"-"),end="")
    print("")
    return False;
def check1TileInQuarter(x,y,field):
    maxFieldX = math.ceil(len(field[0])/2)
    maxFieldY = math.ceil(len(field)/2)
    
    if (x > maxFieldX) or (y > maxFieldY):
        return False
    else:
        return True
def findTopLeft(field):
    for y in range(len(field)):
        for x in range(len(field[y])):
            if(field[y][x] == 0):
                return x,y
    return False;

def isFull(field):
    return findTopLeft(field) == False;

def fits(tile, field, topLeft):
    if (tile.tilenumber == 1):
        if (check1TileInQuarter(topLeft[0],topLeft[1],field) == False):
            return False
    a = tile.width + topLeft[0]  <= len(field[0])
    b = tile.height + topLeft[1]  <= len(field)
    
    if (a and b):
        for x in range(topLeft[0],tile.width+topLeft[0]):
            for y in range(topLeft[1],tile.height+topLeft[1]):
                if not (field[y][x] == 0):
                    return False
    return (a and b)

def placeTile2(tile, field, topLeft):
    newField = copy.deepcopy(field)
    for y in range(len(newField)):
        for x in range(len(newField[y])):
            a = x <= topLeft[0] + tile.width - 1
            b = x >= topLeft[0]
            c = y <= topLeft[1] + tile.height - 1
            d = y >= topLeft[1]
            if(a and b and c and d):
                newField[y][x] = tile.tilenumber
    return newField

def flip(tile):
    return Tile(tile.height, tile.width, tile.tilenumber);
def smallestValley(field):
    coords = []

    for y in range(len(field)):
        same = 0
        minSame = len(field[0])
        
        for x in range(len(field[0])):
            
            if (field[y][x] == 0):
                same += 1
            elif (same > 0):
                if (minSame >= same):
                    minSame = same
                    
                    coords.append((minSame,x-1,y))
                same = 0
        
        if(same > 0):
            if (minSame >= same):
                    minSame = same
                    coords.append((minSame,x,y))

    
    sortedBySize = sorted(coords, key=lambda tup: tup[0])
    
    x = (sortedBySize[0][1]-sortedBySize[0][0]+1)
    y = (sortedBySize[0][2])
    return(x,y)

    
    
def checkMinWidth(field,tileList):
    minWidths = []
    maxWidths = []
    for y in range(len(field)):
        same = 0
        minSame = len(field[0])
        maxSame = 0
        for x in range(len(field[0])):
            if (field[y][x] == 0):
                same += 1
            elif (same > 0):
                if (minSame > same):
                    minSame = same
                if (maxSame < same):
                    maxSame = same            
                same = 0
        if(same > 0):
            if (minSame > same):
                    minSame = same
            if (maxSame < same):
                    maxSame = same
        if(minSame > 0):
            minWidths.append(minSame)
            maxWidths.append(maxSame)

    minWidth = min(minWidths)
    maxWidth= max(maxWidths)
    
    smallestFits = False
    biggestFits = False
    
    for tile in tileList:
         if (min(tile.width,tile.height) <= minWidth):
             smallestFits = True
         if (min(tile.width,tile.height) <= maxWidth):
             biggestFits = True
    
    if (smallestFits) and (biggestFits):
        return True
    
def checkMinHeight(field,tileList):
    rotated = list(zip(*field[::-1]))
    minHeights = []
    maxHeights = []
    for y in range(len(rotated)):
        same = 0
        minSame = len(rotated[0])
        maxSame = 0
        for x in range(len(rotated[0])):
            if (rotated[y][x] == 0):
                same += 1
            elif (same > 0):
                if (minSame > same):
                    minSame = same
                if (maxSame < same):
                    maxSame = same            
                same = 0
        if(same > 0):
            if (minSame > same):
                    minSame = same
            if (maxSame < same):
                    maxSame = same
        if(minSame > 0):
            minHeights.append(minSame)
            maxHeights.append(maxSame)

    minHeight = min(minHeights)
    maxHeight = max(maxHeights)

    smallestFits = False
    biggestFits = False

    for tile in tileList:
         if (min(tile.width,tile.height) <= minHeight):
             smallestFits = True
         if (min(tile.width,tile.height) <= maxHeight):
             biggestFits = True

    if (smallestFits) and (biggestFits):
        return True
def checkFitArea(areaInput,tiles):
    areaSmall = areaInput[0]
    heightSmall = areaInput[1]
    widthSmall = areaInput[2]
    top = areaInput[3]
    fittingTiles = []
    sumWidth = []
    sumHeight = []
    for tile in tiles:
        if (top == True):
            if (max(tile.width,tile.height) <= widthSmall and min(tile.width,tile.height) <= heightSmall) :
                fittingTiles.append(tile)
                sumWidth.append(max(tile.width,tile.height))
                sumHeight.append(min(tile.width,tile.height))
            elif (max(tile.width,tile.height) <= heightSmall and min(tile.width,tile.height) <= widthSmall):   
                fittingTiles.append(tile)
                sumWidth.append(min(tile.width,tile.height))
                sumHeight.append(max(tile.width,tile.height))
        else:
             if (max(tile.width,tile.height) <= widthSmall) :
                fittingTiles.append(tile)
                sumWidth.append(min(tile.width,tile.height))
                sumHeight.append(max(tile.width,tile.height))
             elif (min(tile.width,tile.height) <= widthSmall) :
                fittingTiles.append(tile)
                sumWidth.append(max(tile.width,tile.height))
                sumHeight.append(min(tile.width,tile.height))
    if (len(fittingTiles) == 0):
        return False
    
    if (sum(sumWidth) < widthSmall):
      
        return False
    if (sum(sumHeight) < heightSmall):

        return False


def findArea(tiles,field):
    
    if(len(tiles)<1):
        return
    zeros = list()
    for y in range(len(field)):
        if (0 in field[y]):
            get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
            zeros.append(get_indexes(0,field[y]))
            
    if(len(zeros)<1):
        return
    marker = zeros[0]
    if(len(marker)<tiles[-1].width*2):
        width = len(marker)
        heigth = 0
        for row in zeros:
            if(not marker == row):
                markerStr = str(marker)[1:-1]
                rowStr = str(row)[1:-1]
                if (markerStr in rowStr):
                    if((marker[0]-1 in row) or (marker[-1]+1 in row)):
               
                        return [heigth*width,heigth,width,False];
                    else:
              
                        heigth = heigth + 1;
             
            else:
                heigth = heigth + 1;
     
        return [heigth*width,heigth,width,True];
                        
def placeTile(tiles, field):
    global numberofsolutions, stepsTaken,start_time;

    stepsTaken += 1
    if (numberofsolutions >= 1):
        return
    if isFull(field):
        solutions.append(field)
        numberofsolutions += 1
    
        return

    if(len(tiles) == 0):
        return

    topLeft = smallestValley(field)
    #topLeft = findTopLeft(field)
    oldW = None
    oldH = None
    
    emptySpace = findArea(tiles,field)
    if (emptySpace):
        if (checkFitArea(emptySpace,tiles) == False):
           
           return
    if not (checkMinWidth(field,tiles)):
        return

    if not (checkMinHeight(field,tiles)):
        return

    for tile in tiles:
        if not ((tile.width == oldW) and (tile.height == oldH)) or not ((tile.height == oldW) and (tile.width == oldH)):
                tilesc = list(tiles)
                tilesc.remove(tile)
                oldW = tile.width
                oldH = tile.height
                if fits(tile, field, topLeft):
                    newField = placeTile2(tile, field, topLeft)
                    placeTile(tilesc,newField);
                if(tile.width != tile.height):
                   flippedTile = flip(tile)
                   if(fits(flippedTile, field, topLeft)):
                       newField = placeTile2(flippedTile, field, topLeft)
                       placeTile(tilesc,newField);
    return

times = []


for filename in os.listdir('tilings'):
        file = open("tilings\\"+filename,"r")           

        solutions = []
        stepsTaken = 0
        
        properties = file.readline().rstrip().split(" ")
        widthField = int(properties[1])
        heightField = int(properties[3])
        scaleField = int(properties[5])
        
        coordinateList = [[0 for x in range(widthField)] for y in range(heightField)]
        tileList = []
        tilenumber = 1
        for line in file:
            tileCount = int(line.split(" ")[0])
            widthAndHeight = line.split(" ")[2].split("x")
            width = widthAndHeight[0]
            height = widthAndHeight[1]
        
            for i in range(tileCount):
                tileList.append(Tile(width,height,tilenumber))
                tilenumber += 1
        
        numberofsolutions = 0
        global start_time
        start_time = time.time()
        
        placeTile(tileList,coordinateList)
        run_time = time.time() - start_time
        
        print("Found a solution in: "+str(run_time)+": for file: " +filename +" stepstaken: "+ str(stepsTaken))
        
        times.append(run_time)
        

