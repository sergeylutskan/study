import pygame
size = width, height = 300, 200
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('white'))
clock = pygame.time.Clock()
running = True
x, y = 0, 0
k = 0
def brick(x,y):
    pygame.draw.rect(screen, pygame.Color('red'), [x,y,30,15],0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(0,width,32):
        for j in range(0,height,17):
            k = k +1
            if k % 2==0:
                brick(i,j)
            else:
                brick(i-15,j)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
