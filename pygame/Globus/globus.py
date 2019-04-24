import math
import pygame
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('black'))
clock = pygame.time.Clock()
running = True
# задаем параметры круга
n = int(input())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               running = False
    for i in range(n):
        pygame.draw.ellipse(screen, pygame.Color(255, 255 , 255), [0, i*300/(2*n), 300, 300-i*300/n],1)
        pygame.draw.ellipse(screen, pygame.Color(255, 255 , 255), [i*300/(2*n), 0, 300-i*300/n, 300],1)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
