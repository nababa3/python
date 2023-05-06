from statistics import mean
from PIL import Image
# Read image and extract RGB values of each pixel
im = Image.open('colors.jpg')
pixels = im.load()
colors = [pixels[i, j] for i in range(im.width) for j in range(im.height)]
# Calculate mean RGB values
mean_r = mean([c[0] for c in colors])
mean_g = mean([c[1] for c in colors])
mean_b = mean([c[2] for c in colors])
# Convert mean RGB values to color
mean_color = (int(mean_r), int(mean_g), int(mean_b))
print(f"The mean color is {mean_color}")