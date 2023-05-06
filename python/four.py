from statistics import variance
# Read image and extract RGB values of each pixel
im = Image.open('colors.jpg')
pixels = im.load()
colors = [pixels[i, j] for i in range(im.width) for j in range(im.height)]
# Calculate variance of RGB values
var_r = variance([c[0] for c in colors])
var_g = variance([c[1] for c in colors])
var_b = variance([c[2] for c in colors])
# Print variances
print(f"Variance of red: {var_r}")
print(f"Variance of green: {var_g}")
print(f"Variance of blue: {var_b}")