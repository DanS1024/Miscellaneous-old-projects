import turtle

# Define function
def f(x):
    return x**3 - 3 * x**2 + 2

# Parameters
numIterations = 15 # number of NR iterations
scaleFactor = 100 # general scaling factor
squishFactor = 2 # vertical scaling
xShift = -1
yShift = 0
step = 0.05
deltaX = 1E-4
epsilon = 1E-2

# Screen, Canvas and Turtles setup
scr = turtle.Screen()
scr.title('Newton-Raphson Root Finding')
scr.setup(800, 600)
scr.tracer(0, 0)
cnv = scr.getcanvas()

# Screen coordinates setup
scrHalfW = scr.window_width() / 2
scrHalfH = scr.window_height() / 2
a = -scrHalfW / scaleFactor - xShift
b = scrHalfW / scaleFactor - xShift
c = (-scrHalfH / scaleFactor - yShift) * squishFactor
d = (scrHalfH / scaleFactor - yShift) * squishFactor
scr.setworldcoordinates(a, c, b, d)

# Turtle objects for initial graph and NR iterations
gph = turtle.Turtle()
nwt = turtle.Turtle()
gph.hideturtle()
nwt.hideturtle()

# Initial graph
def graph():
    # Plot axes
    gph.color('lightgray')
    gph.penup()
    gph.goto(a, 0)
    gph.pendown()
    gph.goto(b, 0)
    gph.penup()
    gph.goto(0, c)
    gph.pendown()
    gph.goto(0, d)
    gph.penup()

    # Function
    gph.color('black')
    x = a
    gph.goto(x, f(x))
    gph.pendown()
    while x <= b:
        gph.goto(x, f(x))
        x = x + step
    gph.penup()
    scr.update()


# Newton-Raphson iterations
roots = set()
nwt.color('red')
def newton(pos):
    nwt.clear()

    # mouse x coordinate
    x = pos.x * (b - a) / 2 / scrHalfW + a

    nwt.penup()
    nwt.goto(x, 0)
    nwt.pendown()
    for i in range(numIterations):
        nwt.goto(x, f(x))

        # f'(x) discrete approximation
        fp = (f(x + deltaX) - f(x - deltaX)) / (2 * deltaX)
        # Avoid division by zero
        if abs(fp) < epsilon:
            break
        # NR next iteration
        x = x - f(x) / fp
        nwt.goto(x, 0)
    
    # Add root to set
    if abs(f(x)) < epsilon:
        roots.add(round(x, 4))
    
    scr.update()

# Draw graph and bind mouse motion to NR
graph()
cnv.bind("<Motion>", newton)
scr.mainloop()

# Print roots
print('\nRoots found:', roots, end='\n\n')