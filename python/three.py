# Read image and extract RGB values of each pixel
im = Image.open('colors.jpg')
pixels = im.load()
colors = [pixels[i, j] for i in range(im.width) for j in range(im.height)]
# Convert colors to numeric values
color_values = [int(''.join(map(str, c)), 16) for c in colors]
# Sort colors based on their numeric value
sorted_colors = [colors[i] for i in sorted(range(len(color_values)), key=lambda k:
color_values[k])]
# Find median color
median_index = len(sorted_colors) // 2
median_color = sorted_colors[median_index]
print(f"The median color is {median_color}")