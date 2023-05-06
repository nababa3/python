# Read image and extract RGB values of each pixel
im = Image.open('colors.jpg')
pixels = im.load()
colors = [pixels[i, j] for i in range(im)]