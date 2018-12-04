import copy

def generate_dist_matrix(maze,x1,y1):
    w = len(maze[0])
    h = len(maze)
    new_maze = [[None for i in range(w)] for i in range(h)]
    new_maze[x1][y1] = 1
    stack = [(x1, y1)]
    pen_walls = []
    while stack:
        a, b = stack.pop(0)
        sum = 0
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:

            x, y = a + i[0], b + i[1]

            if 0 <= x < h and 0 <= y < w:

                if new_maze[x][y] is None:
                    new_maze[x][y] = new_maze[a][b] + 1
                    if maze[x][y]:
                        if possible_wall(maze,x,y):
                            pen_walls.append((x,y))
                        continue
                    stack.append((x, y))

    return new_maze, pen_walls

def possible_wall(maze,i,j):
    sum=0
    w=len(maze[0])
    h=len(maze)

    for pair in [[0,1],[1,0],[-1,0],[0,-1]]:
        if 0<= i+pair[0] <h and 0<= j+pair[1] <w:
            sum += maze[i+pair[0]][j+pair[1]]
        else:
            sum+=1

    if sum<3 :
        return True
    else:
        return False

def answer(maze):

    dist_start, pen_walls = generate_dist_matrix(maze,0,0)
    dist_end, pen_walls = generate_dist_matrix(maze,len(maze)-1,len(maze[0])-1)

    min = 2**32-1
    for i in pen_walls:
        if dist_start[i[0]][i[1]] is not None and dist_end[i[0]][i[1]] is not None:
            dist = dist_start[i[0]][i[1]] + dist_end[i[0]][i[1]]
            if min>dist:
                min=dist

    return min-1



maze = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]]
print answer(maze)

