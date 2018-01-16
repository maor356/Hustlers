# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:33:06 2018

@author: Rens
"""

from random import randint
import copy
import os
from colored import fg,bg
 

class Tile:
    x = None
    y = None
    def __init__(self,width,height, tilenumber):
        self.width= int(width)
        self.height = int(height)
        self.tilenumber = int(tilenumber)

def printField(field):
    for y in range(len(field)):
        print("|", end = ""),
        for x in range(len(field[y])):
            print('%s%2d|' % (fg(field[y][x]),field[y][x]), end = "")
        print("\n%s" % (fg('black')), end="")
    return False;

def findTopLeft(field):
    for y in range(len(field)):
        for x in range(len(field[y])):
            if(field[y][x] == 0):
                return x,y
    return False;

def isFull(field):
    return findTopLeft(field) == False;

def fits(tile, field, topLeft):
   
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
def checkMinWidth(field,tileList):
    
    empty = [[0 for col in range(len(field[0]))] for row in range(len(field))]
   
    for y in range(len(field)):
        for i in range(0,len(field[0])):
          

            
            if field[y][i] == 0:
                empty[y][i] = empty[y][i-1] + 1
            else:
                empty[y][i] = 0
    
    minWidth = min(max(empty))
   
    maxWidth= max(max(empty))
    
    smallestFits = False
    biggestFits = True
    for tile in tileList:
         if (min(tile.width,tile.height) >= minWidth):
             smallestFits = True
         if (min(tile.width,tile.height) > maxWidth):
             biggestFits = False
   
    if (smallestFits) and (biggestFits):
        return True
def placeTile(tiles, field):
    
    global numberofsolutions;
    global stepsTaken
    stepsTaken += 1
    
    
    if isFull(field):
        solutions.append(field)
        numberofsolutions += 1
      
        print("Solution %d steps: %d" % (numberofsolutions,stepsTaken))
        printField(field)
        return
    if(len(tiles) == 0):
        return
    topLeft = findTopLeft(field)
    tilesc = list(tiles)
    fieldc = list(field)
    oldW = None
    oldH = None
    if not (checkMinWidth(field,tiles)):
        return
    for tile in tiles:
        if not (tile.width == oldW) and not (tile.height == oldH) and not (tile.height == oldW) and not (tile.width == oldH):
            oldW = tile.width
            oldH = tile.height
            if fits(tile, field, topLeft):
                newField = placeTile2(tile, field, topLeft)
                tilesc.remove(tile)
                placeTile(tilesc,newField);
                tilesc.append(tile)
            if(tile.width != tile.height):
                flippedTile = flip(tile)
                if(fits(flippedTile, field, topLeft)):
                    newField = placeTile2(flippedTile, fieldc, topLeft)
                    tilesc.remove(tile)
                    placeTile(tilesc,newField);
                    tilesc.append(tile)
        
    return


    
file = open("tilings/15-0-0.tiles","r")
solutions = []
stepsTaken = 0

properties = file.readline().rstrip().split(" ")
widthField = int(properties[1])
heightField = int(properties[3])
scaleField = int(properties[5])

coordinateList = [[0 for x in range(heightField)] for y in range(widthField)]
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
placeTile(tileList,coordinateList);
print("Found %d solutions" % numberofsolutions)
def printTiles(tiles):
    x = 1
    for tile in tiles:
        print("Tile %d - %d x %d" % (x, tile.width, tile.height))
        x += 1
printTiles(tileList)

