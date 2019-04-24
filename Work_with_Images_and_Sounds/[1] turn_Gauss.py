# Повернуть изображение и сделать размытие по Гауссу
# Rotate the image and make a Gaussian blur

from PIL import Image, ImageDraw, ImageFilter

def motion_blur(n):

    im = Image.open("image.JPG")
    im = im.transpose(Image.ROTATE_270) 
    im = im.filter(ImageFilter.GaussianBlur(radius=n))
    im.save("res.jpg")

 
motion_blur(int(input()))

