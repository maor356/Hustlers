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

def findTopLeft(field):
    for y in range(len(field)):
        for x in range(len(field[y])):
            if(field[y][x] == 0):
                return x,y
    return False;

def isFull(field):
    return findTopLeft(field) == False;

def fits(tile, field, topLeft):
    return (tile.width + topLeft[0] <= len(field) and tile.height + topLeft[1] <= len(field[0]))

def placeTile2(tile, field, topLeft):
    for y in range(len(field)):
        for x in range(len(field[y])):
            a = x <= topLeft[0] + tile.width
            b = x >= topLeft[0]
            c = y <= topLeft[1] + tile.height
            d = y >= topLeft[1]
            if(a and b and c and d):
                field[y][x] == 1
    return field

def placeTile(tiles, field):
    if isFull(field):
        print("FOUND A SOLUTION")
        return;
    print("a")

    topLeft = findTopLeft(field);

    for tile in tiles:
        if fits(tile, field, topLeft):
            newField = placeTile2(tile, field, topLeft)
            placeTile(tiles.remove(tile),newField);

            if(tile.width != tile.height):
                flippedTile = flip(tile)
                if(fits(flippedTile, field, topLeft)):
                    newField = placeTile2(flippedTile, field, topLeft)
                    # newTiles = tiles.remove(tile)
                    placeTile(tiles,newField);

file = open("simple.tiles","r")
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

placeTile(unusedTiles,coordinateList);
