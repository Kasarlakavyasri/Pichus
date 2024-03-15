#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : KAVYA SRI KASARLA - kkasarla
#
# Based on skeleton code in CSCI B551, Fall 2022.

import sys

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])
    
# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if (house_map[r][c] == '.' and Diag_check(house_map,r,c) and RowCol_check(house_map,r,c)) ]  #added function to check the diagonals as well rowas and colums to validate the pichu position

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

def RowCol_check(house_map,r,c): #function to check up,down,left,right
    return Ucheck(house_map,r,c) and Dcheck(house_map,r,c) and Lcheck(house_map,r,c) and Rcheck(house_map,r,c)
    
def Ucheck(house_map,r,c): 
    if(0<=r<len(house_map) and (0<= c <len(house_map[0]))):
        if house_map[r][c] in "X@":
            return True
        elif house_map[r][c]=="p":
            return False
        else:
            return Ucheck(house_map,r-1,c)
    return True

def Dcheck(house_map,r,c):
    if(0<=r<len(house_map) and (0<= c <len(house_map[0]))):
        if house_map[r][c] in "X@":
            return True
        elif house_map[r][c]=="p":
            return False
        else:
            return Dcheck(house_map,r+1,c)
    return True
def Lcheck(house_map,r,c):
    if(0<=r<len(house_map) and (0<= c <len(house_map[0]))):
        if house_map[r][c] in "X@":
            return True
        elif house_map[r][c]=="p":
            return False
        else:
            return Lcheck(house_map,r,c-1)
    return True
def Rcheck(house_map,r,c):
    if(0<=r<len(house_map) and (0<= c <len(house_map[0]))):
        if house_map[r][c] in "X@":
            return True
        elif house_map[r][c]=="p":
            return False
        else:
            return Rcheck(house_map,r,c+1)
    return True

def Diag_check(house_map,r,c):  #function to check diagonals
    return UpperLeft(house_map,r,c) and UpperRight(house_map,r,c) and LowerLeft(house_map,r,c) and LowerRight(house_map,r,c)
     
def UpperLeft(house_map,r,c):
    if(0<=r<len(house_map) and (0<= c <len(house_map[0]))):
        if house_map[r][c] in "X@":
            return True
        elif house_map[r][c]=="p":
            return False
        else:
            return UpperLeft(house_map,r-1,c-1)
    return True
def UpperRight(house_map,r,c):
    if(0<=r<len(house_map) and (0<= c <len(house_map[0]))):
        if house_map[r][c] in "X@":
            return True
        elif house_map[r][c]=="p":
            return False
        else:
            return UpperRight(house_map,r-1,c+1)
    return True
def LowerLeft(house_map,r,c):
    if(0<=r<len(house_map) and (0<= c <len(house_map[0]))):
        if house_map[r][c] in "X@":
            return True
        elif house_map[r][c]=="p":
            return False
        else:
            return LowerLeft(house_map,r+1,c-1)
    return True
def LowerRight(house_map,r,c):
    if(0<=r<len(house_map) and (0<= c <len(house_map[0]))):
        if house_map[r][c] in "X@":
            return True
        elif house_map[r][c]=="p":
            return False
        else:
            return LowerRight(house_map,r+1,c+1)
    return True  
    

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):   
      
    fringe = [initial_house_map]
    traversed=[]
    if (k==1) and is_goal(initial_house_map,k): 
        return (initial_house_map,True)
    while len(fringe) > 0:        
        for new_house_map in successors(fringe.pop()):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            else:
                if new_house_map not in traversed:
                    fringe.append(new_house_map)
                    traversed.append(new_house_map)
    return (new_house_map,False)

    

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


#python arrange_pichus.py map1.txt 3
#python arrange_pichus.py map2.txt 2