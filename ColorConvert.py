from PIL import Image

picture = Image.open("./input/face.png")
RgbPicture = picture.convert('RGB')
ColorPalette = [(0, 0, 0), (255, 255, 255), (128, 128, 128)]


def colordist(color):
  r1, g1, b1 = color
  lastdistance = float('inf')
  d = 0

  for x in ColorPalette:
    r2, g2, b2 = x
    d = ((r2 - r1) * 0.30)**2 + ((g2 - g1) * 0.59)**2 + ((b2 - b1) * 0.11)**2
    if d < lastdistance:
      lastdistance = d
      color = x
  return color


y = 0
for y in range(picture.height):
  for x in range(picture.width):
    coordinate = x, y
    picture.putpixel(coordinate, colordist(RgbPicture.getpixel(coordinate)))

picture.save("hello.png")
