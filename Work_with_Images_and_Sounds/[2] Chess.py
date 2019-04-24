# Create a chessboard by two parameters: the number of cells and their size

from PIL import Image, ImageDraw

def board(num,size):
    # создание изображения  
    new_image = Image.new("RGB", (num*size, num*size), (0, 0, 0))  
    # на изображении создаем рисунок для рисования  
    draw = ImageDraw.Draw(new_image)  

    for i in range(num):
        for j in range(num):
            if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                draw.rectangle([i*size,j*size,i*size+size,j*size+size], fill=(255, 255, 255))

    # сохраним изображением в файл формата PNG  
    new_image.save('res.png', 'PNG')
 

board(10,50)


