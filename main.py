from PIL import Image

im = Image.open('new_year.jpg')
width = im.size[0]
height = im.size[1]

print('width is ' + str(width),'height is ' + str(height))

