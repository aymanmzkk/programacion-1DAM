from PIL import Image

img = Image.open("milky_star_cookie.jpg")

pixel1 = img.getpixel((0,0))

print(pixel1)
