import colorgram

# extract rgb colors from painting
rgb_colors = []
colors = colorgram.extract("damien-hirst-painting.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b)
    rgb_colors.append(rgb_color)



