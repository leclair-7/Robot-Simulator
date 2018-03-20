# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------
from pprint import pprint


'''
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right
'''
delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost,heuristic):
    '''
    Implements A* search
    '''
    delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right
    #what does closed, expand and action mean
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    count = 0
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            
            a=open[0][1]
            b=open[0][2]
            minim=open[0]
            mini = open[0][0] + heuristic[a][b]
            for i in open[1:]:
                if i[0] + heuristic[i[1]][i[2]] < mini:
                    minim=i
            
            next = minim
            open.remove(minim)
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
    return expand


if __name__=='__main__':

    grid = [[0, 1,  0, 0, 0],
            [0, 1,  0, 0, 0],
            [0, 1,  0, 0, 0],
            [0, 1,  0, 0, 0],
            [0, 0,  0, 1, 0]]

    heuristic = [[9, 8, 6, 5, 4],
                 [8, 7, 5, 4, 3],
                 [7, 6, 4, 3, 2],
                 [6, 5, 3, 2, 1],
                 [5, 4, 2, 1, 0]]
    init = [4, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1
    pprint(search(grid,init,goal,cost,heuristic) )