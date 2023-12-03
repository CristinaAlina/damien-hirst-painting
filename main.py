import colorgram

# extract rgb colors from painting
rgb_colors = []
colors = colorgram.extract("damien-hirst-painting.jpg", 30)
for color in colors:
    rgb_colors.append(color.rgb)
