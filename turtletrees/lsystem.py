import string
import turtle


def generate(string, max_iter):
    for step in range(max_iter):
        string = reproduce(string)
    return string


def reproduce(string):
    new = ''
    for character in string:
        if character == 'A':
            new += 'B[+A]-A'
        elif character == 'B':
            new += 'B'
        else:
            new += character
    return new


def draw(t, s, length, angle):
    '''moves drawing turtle across the canvas'''
    stack = []
    for character in s:
        if character in string.ascii_letters:
            t.forward(length)
        elif character == '-':
            t.left(angle)
        elif character == '+':
            t.right(angle)
        elif character == '[':
            pos = t.position()
            head = t.heading()
            stack.append((pos, head))
        elif character == ']':
            prior_position, prior_heading = stack.pop()
            t.penup()
            t.goto(prior_position)
            t.setheading(prior_heading)
            t.pendown()


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
    angle = 36
    max_iter = 8

    # print(generate(axiom, max_iter))
    draw(t, generate(axiom, max_iter), length, angle)

    wn.exitonclick()


main()
