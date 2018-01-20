import time
import copy

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
    elif not (checkMinHeight(field,tiles)):
        
        return
    for tile in tiles:

        if not ((tile.width == oldW) and (tile.height == oldH)) or not ((tile.height == oldW) and (tile.width == oldH)):
               
                oldW = tile.width
                oldH = tile.height
                if fits(tile, field, topLeft):
                    newField = placeTile2(tile, field, topLeft)
                    tilesc.remove(tile)
                    placeTile(tilesc,newField);
                    tilesc = list(tiles)
                if(tile.width != tile.height):
                    flippedTile = flip(tile)
                    if(fits(flippedTile, field, topLeft)):
                        newField = placeTile2(flippedTile, fieldc, topLeft)
                        tilesc.remove(tile)
                        placeTile(tilesc,newField);
                        tilesc = list(tiles)
    return

file = open("test.tiles","r")

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

start_time = time.time()
placeTile(tileList,coordinateList);
run_time = time.time() - start_time

print("Found %d solutions" % numberofsolutions)
def printTiles(tiles):
    x = 1
    for tile in tiles:
        print("Tile %d - %d x %d" % (x, tile.width, tile.height))
        x += 1
printTiles(tileList)
print("--- %s seconds ---" % run_time)
