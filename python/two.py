from collections import Counter
# Read image and extract RGB values of each pixel
im = Image.open('colors.jpg')
pixels = im.load()
colors = [pixels[i, j] for i in range(im.width) for j in range(im.height)]
# Count frequency of each color
color_counts = Counter(colors)
# Get color with highest frequency
most_common_color = color_counts.most_common(1)[0][0]
print(f"The color worn most frequently is {most_common_color}")