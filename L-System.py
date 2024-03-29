import math, turtle
turtle.setup(640, 640)
turtle.bgcolor('black')
turtle.tracer(0, 0)
t = turtle.Turtle()
t.color('white')
t.hideturtle()

def generate():
    global text, n
    for k in range(n):
        newText = ''
        for i in text:
            try:
                newText += rules.get(i)
            except:
                newText += i
        text = newText

def start(x, y, orientation):
    global t
    t.penup()
    t.setheading(orientation)
    t.goto(x, y)
    t.pendown()

states = []
def getT():
    global t, states
    states.append((t.heading(), t.position()))

def setT():
    global t, states
    state = states[-1]
    t.penup()
    t.setheading(state[0])
    t.setposition(state[1][0], state[1][1])
    states = states[:-1]
    t.pendown()



## Fractal Plant 1

text = 'X'
rules = {'X':'F+[[X]-X]-F[-FX]+X', 'F':'FF'}
angle = 25

n = 6
generate()
start(-300, -300, 60)

for i in text:
    if i == 'F':
        t.forward(4)
    elif i == '-':
        t.right(angle)
    elif i == '+':
        t.left(angle)
    elif i == '[':
        getT()
    elif i == ']':
        setT()



## Fractal Tree 1

##text = 'F'
##rules = {'F':'FF+[+F-F-F]-[-F+F+F]'}
##angle = 25
##
##n = 5
##generate()
##start(0, -300, 90)
##
##for i in text:
##    if i == 'F':
##        t.forward(5)
##    elif i == '-':
##        t.right(angle)
##    elif i == '+':
##        t.left(angle)
##    elif i == '[':
##        getT()
##    elif i == ']':
##        setT()



## Fractal (Binary) Tree

##text = 'A'
##rules = {'A':'B[A]A', 'B':'BB'}
##angle = 35
##
##n = 8
##generate()
##start(0, -300, 90)
##
##for i in text:
##    if i == 'A' or i == 'B':
##        t.forward(600/(2**n))
##    elif i == '[':
##        getT()
##        t.left(angle)
##    elif i == ']':
##        setT()
##        t.right(angle)



## Dragon Curve

##text = 'FX'
##rules = {'X':'X+YF+', 'Y':'-FX-Y'}
##angle = 90
##
##n = 12
##generate()
##start(-500/3, -200/3, (45*n)%360)
##
##for i in text:
##    if i == 'F':
##        t.forward(400/(2**(n/2)))
##    elif i == '+':
##        t.right(angle)
##    elif i == '-':
##        t.left(angle)



## Serpinski's Triangle

##text = 'A'
##rules = {'A':'B-A-B', 'B':'A+B+A'}
##angle = 60
##
##n = 6
##generate()
##if n%2 == 0:
##    start(-300, -300, 0)
##else:
##    start(-300, -300, 60)
##
##for i in text:
##    if (i == 'A') or (i == 'B'):
##        t.forward(600/(2**n))
##    elif i == '+':
##        t.left(angle)
##    elif i == '-':
##        t.right(angle)



turtle.update()
turtle.done()