import pygame
size = width, height = 100, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('yellow'))
clock = pygame.time.Clock()
running = True
n = int(input())
x, y = 0, 0

def romb(x,y,n):
    pygame.draw.polygon(screen, pygame.Color('orange'), [(x,y+n/2),(x+n/2,y),(x+n,y+n/2),(x+n/2,y+n)],0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(0,width,n):
        for j in range(0,height,n):
            romb(i,j,n)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
