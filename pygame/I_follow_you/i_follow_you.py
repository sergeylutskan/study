import pygame
# инициализация Pygame:
def draw(q):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100) # шрифт по-умолчанию
    text = font.render(str(q), 1, (255, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))



pygame.init()
# размеры окна: 
size = width, height = 200, 200
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
running = True
q = 1
draw(q)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if pygame.display.get_active()==False:
            q +=1
            draw(q)
            pygame.display.flip()
                
    pygame.display.flip()
pygame.quit()

