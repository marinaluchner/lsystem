import string
import turtle
IABCA
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
            new += 'A-A++A-AB'
        elif c == 'B':
            new += '--AB'
    return new

def draw(t, s, length, angle):
    for c in s:
        if c in string.ascii_letters:
            t.forward(length)
        elif c == '-':
            t.left(angle)
        elif c == '+':
            t.right(angle)

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

    axiom = 'AB-B++B'
    length = 10
    angle = 56
    iterations = 4

    print(lSysGenerate(axiom, iterations))
    draw(t, lSysGenerate(axiom, iterations), length, angle)

    wn.exitonclick()

main()