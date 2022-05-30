# Script to solve day 5 of Advent of Code

# Plots lines of vents from the coordinates contained in day5_input.txt
# Returns the number of coordinates with 2 or more overlapping vent lines


# Import libraries
import numpy as np
import io


## Define Functions

# create map from max xy dimensions
def make_map(vents):
    global map
    x_dim = vents[:, :, 0].max() + 1
    y_dim = vents[:, :, 1].max() + 1
    map = np.zeros((x_dim, y_dim))

# select pairs of coordinates xx, yy from line number
def xx(line_no):
    return vents[line_no,:,0]

def yy(line_no):
    return vents[line_no,:,1]

# check orientation of vent line
def orientation(line_no):
    if np.all(vents[line_no,0,0] == vents[line_no,1,0]): # check if x coordinates are equal
        return "X"
    elif np.all(vents[line_no,0,1] == vents[line_no,1,1]): # check if y coordinates are equal
        return "Y"
    else:
        return "Diagonal"

# check direction of diagnoal vent line
def find_xy_of_min_x(line_no):
    # Return xy coordinates of pair with lowest x 
    if vents[line_no,0,0] > vents[line_no,1,0]:
        return vents[line_no,1,:]
    elif vents[line_no,0,0] < vents[line_no,1,0]:
        return vents[line_no,0,:]
    else:
        return "error"

def find_xy_of_max_x(line_no):
    # Return xy coordinates of pair with highest x
    if vents[line_no,0,0] < vents[line_no,1,0]:
        return vents[line_no,1,:]
    elif vents[line_no,0,0] > vents[line_no,1,0]:
        return vents[line_no,0,:]
    else:
        return "error"

def ascending_or_descending(line_no):
    # Determine if diagonal is ascending or descending
    y1 = find_xy_of_min_x(line_no)[1]
    y2 = find_xy_of_max_x(line_no)[1]
    if y1 < y2:
        return "ascending"
    elif y1 > y2:
        return "descending"

# mark vent lines on map
def if_Y(line_no):
    # if orientation is Y, add 1 to (x1 -> x2, y)
    x_min = xx(line_no).min()
    x_max = xx(line_no).max()+1
    y = yy(line_no)[0]
    for x in range(x_min, x_max):
        map[x,y] = map[x,y]+1

def if_X(line_no):
    # if orientation is X, add 1 to (x, y1 -> y2)
    y_min = yy(line_no).min()
    y_max = yy(line_no).max()+1
    x = xx(line_no)[0]
    for y in range(y_min, y_max):
        map[x,y] = map[x,y]+1

def if_ascending(line_no):
    # +1 to each point from xy1 to xy2 on map in ascending diagonal
    x = find_xy_of_min_x(line_no)[0]
    y = find_xy_of_min_x(line_no)[1]
    y2 = find_xy_of_max_x(line_no)[1]
    while y <= y2:
        map[x,y] = map[x,y]+1
        x = x+1
        y = y+1

def if_descending(line_no):
    # +1 to each point from xy1 to xy2 in descending diagnoal
    x = find_xy_of_min_x(line_no)[0]
    y = find_xy_of_min_x(line_no)[1]
    y2 = find_xy_of_max_x(line_no)[1]
    while y >= y2:
        map[x,y] = map[x,y]+1
        x = x+1
        y = y-1


# Main function

def main():
    # read data
    with open('day5_input.txt') as f:
        global vents
        vents = np.loadtxt((x.replace('->',',') for x in f),delimiter=',', dtype=int)
        vents = np.reshape(vents, (-1, 2, 2))

    # Create map
    make_map(vents)

    # Mark locations of vent lines on map
    for line_no in range(len(vents)):
        axis = orientation(line_no)
        if axis == 'Y':
            if_Y(line_no)
        elif axis == 'X':
            if_X(line_no)
        elif axis == 'Diagonal':
            pass
            direction = ascending_or_descending(line_no)
            if direction == 'ascending':
                if_ascending(line_no)
            elif direction == 'descending':
                if_descending(line_no)

    # Count values >= 2 on map
    print(np.count_nonzero(map>=2))

if __name__ == '__main__':
    main()
