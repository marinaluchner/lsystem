import string
import turtle


A_rule = 'B+[[A]-A]-B[-BA]+A'
B_rule = 'BA'

def generate(string, max_iter,  A_rule, B_rule):
    for step in range(max_iter):
        string = reproduce(string, A_rule, B_rule)
    return string

def reproduce(self, string, A_rule, B_rule):
    new = ''
    for character in string:
        if character == 'A':
            new += A_rule
        elif character == 'B':
            new += B_rule
        else:
            new += character
    return new


# def draw(t, s, length, angle):
#     '''moves drawing turtle across the canvas'''
#     stack = []
#     for character in s:
#         if character in string.ascii_letters:
#             t.forward(length)
#         elif character == '-':
#             t.left(angle)
#         elif character == '+':
#             t.right(angle)
#         elif character == '[':
#             pos = t.position()
#             head = t.heading()
#             stack.append((pos, head))
#         elif character == ']':
#             prior_position, prior_heading = stack.pop()
#             t.penup()
#             t.goto(prior_position)
#             t.setheading(prior_heading)
#             t.pendown()


# def main():
#     t = turtle.Turtle()
#     wn = turtle.Screen()
#     wn.bgcolor('black')
#     t.speed('fastest')
#     t.hideturtle()
#     t.color('white')
#     t.pensize(5)
#     t.penup()
#     t.setpos(-10, -10)
#     t.pendown()
#     t.speed(0)

#     axiom = 'A+[A]B-'
#     length = 10
#     angle = 23
#     max_iter = 6

#     # print(generate(axiom, max_iter))
#     draw(t, generate(axiom, max_iter), length, angle)

#     wn.exitonclick()


# #main()
