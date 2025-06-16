import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract("k.jpg", 6)

# Print the RGB values of the extracted colors.
print(colors)