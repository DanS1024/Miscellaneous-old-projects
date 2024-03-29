import random, sys, time
import turtle



n = 100

draw = 1


print('Generating then solving a square maze of side', n)

sys.setrecursionlimit(10000)


## Generate the maze using backtracking


def genMaze(n):
    grid = [[1, 1, 1, 1] for i in range(n*n)]
    visit = n*n*[0]
    stack = [[0, 0]]

    x, y = 0, 0
    visit[0] = 1

    for i in range(2*n*n-1):
        newPos = [[x+1, y], [x, y-1], [x-1, y], [x, y+1]]
        
        neighbors = [visit[newPos[0][0] + newPos[0][1]*n] if x != n-1 else None,
                     visit[newPos[1][0] + newPos[1][1]*n] if y != 0   else None,
                     visit[newPos[2][0] + newPos[2][1]*n] if x != 0   else None,
                     visit[newPos[3][0] + newPos[3][1]*n] if y != n-1 else None]

        unvisited = []
        for index in range(4):
            if neighbors[index] == 0:
                unvisited.append(index)
        
        try:
            nextIndex = random.choice(unvisited)
            grid[x + y*n][nextIndex] = 0
            x, y = newPos[nextIndex][0], newPos[nextIndex][1]
            grid[x + y*n][(nextIndex + 2) % 4] = 0
            stack.append([x, y])
            visit[x + y*n] = 1
        except:
            newCurrent = stack.pop()
            x, y = newCurrent[0], newCurrent[1]
    return grid

startTime = time.time()
grid = genMaze(n)
endTime = time.time()

print('Maze Generation Time:', endTime - startTime)










## Solve the maze


visit = n*n*[0]
def _mover(x, y, path):
    global grid, visit, n
    selfX, selfY = x, y
    selfPath = path.copy()
    while True:
        selfPath.append([selfX, selfY])
        visit[selfX + selfY*n] = 1
        walls = grid[selfX + selfY*n]
        if selfX == n-1 and selfY == n-1:
            return selfPath.copy()
        else:
            available = []
            newPos = [[selfX+1, selfY],
                      [selfX, selfY-1],
                      [selfX-1, selfY],
                      [selfX, selfY+1]]
            for i in range(4):
                if walls[i] == 0 and visit[newPos[i][0]+newPos[i][1]*n] == 0:
                    available.append(i)
            if len(available) == 0:
                break
            selfX, selfY = newPos[available[0]][0], newPos[available[0]][1]
            available = available[1:]
            for i in available:
                res = _mover(newPos[i][0], newPos[i][1], selfPath)
                if res != 0:
                    return res
    return 0

def mover():
    visit = n*n*[0]
    return _mover(0, 0, [])


startTime = time.time()
solved = mover()
endTime = time.time()
print('Maze Solving Time:   ', endTime - startTime)



## Draw the maze

if draw:
    turtle.setup(800, 800)
    turtle.setworldcoordinates(-2, n+1, n+1, -2)
    turtle.bgcolor('black')
    turtle.tracer(0, 0)
    t = turtle.Turtle()
    t.speed(100000)
    t.color('white')
    t.penup()
    t.hideturtle()

    w = 0.5

    startTime = time.time()
    
    for y in range(n):
        for x in range(n):
            walls = grid[x + y*n]
            pos = [(x+w, y+w),
                   (x+w, y-w),
                   (x-w, y-w),
                   (x-w, y+w)]
            for i in range(4):
                if walls[i]:
                    t.goto(*pos[i])
                    t.pendown()
                    t.goto(*pos[(i+1)%4])
                    t.penup()



    t.color('cyan')
    t.goto(0, 0)
    t.pendown()
    for crd in solved:
        t.goto(*crd)

    turtle.update()

    endTime = time.time()
    print('Maze Rendering Time: ', endTime - startTime)

print('Done')
turtle.Screen().exitonclick()