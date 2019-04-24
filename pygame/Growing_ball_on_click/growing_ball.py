import pygame

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
# Красим фон
screen.fill(pygame.Color('blue'))
x1, y1 = 0, 0
circle_exists = False  # переменная указывает на существование круга
plus_radius = 2  # номер нашего созданного события
# таймер вызова события увеличения радиуса круга
pygame.time.set_timer(plus_radius, 100)
r = 10

def circle():
    pygame.draw.circle(screen, (255, 255, 0), [x1,y1],r, 0)
    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # реакция на нажатие мыши
        if event.type == pygame.MOUSEBUTTONUP:
            # красим фон и поверх него рисуем новый круг
            r = 10
            # Запоминаем координаты мыши
            x1, y1 = event.pos  
            screen.fill(pygame.Color('blue'))
            circle()
            cirle_exists = True
            pygame.display.flip()
            
            
        if event.type == plus_radius: # Событие увеличения радиуса круга
            r = r + 1
            circle()
            pygame.display.flip()

    if circle_exists:
        circle()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
