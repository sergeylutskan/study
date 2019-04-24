# Уменьшить картинку и уменьшить глубину цвета картинки (сделать preview)
# Reduce the image and reduce the color depth of the image (make a preview)

from PIL import Image, ImageDraw, ImageFilter

def make_preview(size, n_colors) :

    im = Image.open("image.JPG")
    im = im.quantize(n_colors)
    im.thumbnail(size)

    im.save("preview.bmp")


make_preview((400, 200), 2)  

