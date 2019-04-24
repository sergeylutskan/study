# Create a gradient picture filled one of three colours (R,G,B)

from PIL import Image, ImageDraw

def gradient(color):
    # создание изображения  
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))  
    # на изображении создаем рисунок для рисования  
    draw = ImageDraw.Draw(new_image)  
     

    if color.lower() == 'r':
        for i in range(512):
            draw.line((i, 0, i, 200), fill=(i//2, 0, 0), width=1)
    elif color.lower() == 'g':
        for i in range(512):
            draw.line((i, 0, i, 200), fill=(0, i//2, 0), width=1)
    elif color.lower() == 'b':
        for i in range(512):
            draw.line((i, 0, i, 200), fill=(0, 0, i//2), width=1)
    else:
        return 'Неверный цвет'

    # сохраним изображением в файл формата PNG  
    new_image.save('res.png', 'PNG')
 

gradient('G')


