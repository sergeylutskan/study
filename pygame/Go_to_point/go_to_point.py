import pygame

size = width, height = 501, 501
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
# Красим фон
screen.fill(pygame.Color('black'))
x1, y1 = 250, 250
xn, yn = 250, 250
pygame.draw.circle(screen, (255, 0, 0), [x1,y1],20, 0)
go = 2  # номер нашего созданного события
# таймер вызова события следования
pygame.time.set_timer(go, 100)


def circle():
    pygame.draw.circle(screen, (255, 0, 0), [xn,yn],20, 0)
    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # реакция на нажатие мыши
        if event.type == pygame.MOUSEBUTTONUP:
            # Запоминаем координаты мыши
            x1, y1 = event.pos  
            screen.fill(pygame.Color('black'))
            
            
            pygame.display.flip()
            
            
        if event.type == go: # Событие увеличения радиуса круга
            
            while xn != x1:
                if xn > x1:
                    xn -=1
                elif xn < x1:
                    xn+=1
                if yn > y1:
                    yn -=1
                elif yn < y1:
                    yn+=1
                screen.fill(pygame.Color('black'))
                circle()
            while yn != y1:
                if xn > x1:
                    xn -=1
                elif xn < x1:
                    xn+=1
                if yn > y1:
                    yn -=1
                elif yn < y1:
                    yn+=1    
                screen.fill(pygame.Color('black'))
                circle()
            pygame.display.flip()


    pygame.display.flip()
    clock.tick(50)
pygame.quit()
