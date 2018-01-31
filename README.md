# Perfect fit tiling problem

This project is for the course Heuristics on the Vrije Universiteit of Amsterdam. 
The task is to write an algorithm that effeciently find ways to perfectly put tiles in a field.

## Getting Started

### Prerequisites
This project uses Python 3 and the colored library.
Install this library with pip:
```
$ pip install colored
```

### Input file 

The file should look like this:
```
width: WIDTHFIELD height: HEIGHTFIELD scale: RANDOMNUMBER
NumberOfTimesThisTileOccurs times WidthTilexHeightTile
NumberOfTimesThisTileOccurs times WidthTile2xHeightTile2
...

```

An example of a good input file is:

```
width: 12 height: 12 scale: 20
3 times 4x4
9 times 4x2
2 times 3x2
1 times 2x2
4 times 2x1
```



## Running it
Use coloredversion.py to find the solution of an individual file.
Search for this line in the file to input your own tiling problem.
```
file = open("filename.tiles","r")
```

## Finding a solution for multiple files
The file Timeto1stsolutionfiles.py enables you to find a solution for all files in the map tilings.
Watchout! It will continue with a file till it finds a solution. This can take a LONG time.

## Authors

* **Rens Hakkesteegt**
* **Maor Ben Zvi**
* **Jean Louis Le**
* **Iliya Georgiev**
