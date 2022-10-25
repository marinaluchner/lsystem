import string
import turtle
#IABCA
def lSysGenerate(s, order):
    for i in range(order):
        s = reproduce(s)
    return s

def reproduce2(s):
    d = {'A': 'A-A++A-A'}
    return ''.join([d.get(c) or c for c in s])

def  reproduce(s):
# Easier to understand than reproduce2()
    new = ''
    for c in s:
        if c == 'A':
            new += 'B[+A]-A'
        elif c == 'B':
            new += 'BB'
    return new

def draw(t, s, length, angle):
    '''moves drawing turtle across the canvas'''
    stack = []
    for c in s:
        if c in string.ascii_letters:
            t.forward(length)
        elif c == '-':
            t.left(angle)
        elif c == '+':
            t.right(angle)
        elif c == '[':
            pos = t.position()
            head = t.heading()
            stack.append(pos, head)
        elif c == ']':
            prior_position = stack[-1][0]
            prior_heading = stack[-1][1]
            t.penup()
            t.goto(prior_position)
            t.setheading(heading)
            t.pendown()
            stack.pop()
            

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('black')
    t.color('orange')
    t.pensize(1)
    t.penup()
    t.setpos(-10, -10)
    t.pendown()
    t.speed(0)

    axiom = 'ABAB'
    length = 10
    angle = 56
    iterations = 4

    print(lSysGenerate(axiom, iterations))
    draw(t, lSysGenerate(axiom, iterations), length, angle)

    wn.exitonclick()

main()