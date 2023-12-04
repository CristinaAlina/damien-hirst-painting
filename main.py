# import colorgram
#
# # extract rgb colors from painting
# rgb_colors = []
# colors = colorgram.extract("damien-hirst-painting.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)

import random
import turtle as t
# use directly the resulted tuples list of colors without white shades
rgb_colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

turtle = t.Turtle()

t.colormode(255)
turtle.speed("fastest")
turtle.hideturtle()

# set the dot requirements
dot_size = 20
dot_gap = 50

# set initial coordinates of turtle position starting from the lowest point
x_axis = -200
y_axis = -200
turtle.penup()

for index_row in range(10):
    # set the starting position of each row, going up one step at each iteration
    turtle.setpos(x_axis, y_axis + dot_gap * index_row)
    # draw 10 dots per row
    for _ in range(10):
        color = random.choice(rgb_colors)
        turtle.pendown()
        turtle.dot(dot_size, color)
        turtle.penup()
        turtle.forward(50)


t.exitonclick()