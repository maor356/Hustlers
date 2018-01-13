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
    def __init__(self,width,height, tilenumber):
        self.width= int(width)
        self.height = int(height)
        self.tilenumber = int(tilenumber)

def sum2darray(input):
    return sum(map(sum, input))

def printField(field):
    for y in range(len(field)):
        print("|", end = ""),
        for x in range(len(field[y])):
            print("%d |" % field[y][x], end = "")
        print("\n", end="")
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
    a = tile.width + topLeft[0]  <= len(field)
    b = tile.height + topLeft[1]  <= len(field[0])
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

def placeTile(tiles, field):
    global numberofsolutions;
    if isFull(field):
        numberofsolutions += 1
        print("Solution %d" % numberofsolutions)
        printField(field)
        return
    if(len(tiles) == 0):
        return
    topLeft = findTopLeft(field)
    tilesc = list(tiles)
    fieldc = list(field)
    for tile in tiles:
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

file = open("mid.tiles","r")

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
