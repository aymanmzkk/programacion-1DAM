from PIL import Image

imagen = Image.open("milky_star_cookie.jpg")

anchura,altura = imagen.size      # Cojo altura y anchura

for x in range(0,anchura):        # Repaso la anchura
 for y in range(0,altura):        # Repaso la altura
  pixel1 = imagen.getpixel((x,y)) # Cojo cada pixel
  print(pixel1)                   # Y lo saco por pantalla

