import pygame
pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
left = 100 
top = 100
cell_size = 50
width = 5
height = 7
b = [[0] * width for _ in range(height)]
e = []

class Board:
    k = True
    def __init__(self, width, height):
        pass
    def render(self):
        #colors = [pygame.Color("black"), pygame.Color("white")]
        for y in range(height):
            for x in range(width):
                pygame.draw.rect(screen, pygame.Color("black"), (x * cell_size + left, y * cell_size + top, cell_size, cell_size))
                pygame.draw.rect(screen, pygame.Color("white"), (x * cell_size + left, y * cell_size + top, cell_size, cell_size), 1)    
    def cross(self,cell):
        pygame.draw.line(screen,pygame.Color('blue'),(cell[0]*cell_size+2+left,cell[1]*cell_size+2+top),(cell[0]*cell_size+cell_size-2+left,cell[1]*cell_size+cell_size-2+top))
        pygame.draw.line(screen,pygame.Color('blue'),(cell[0]*cell_size+2+left,cell[1]*cell_size+cell_size-2+top),(cell[0]*cell_size+cell_size-2+left,cell[1]*cell_size+2+top))
        e.append(cell)
        self.k = False
    def criss(self,cell):
        pygame.draw.circle(screen,pygame.Color('red'),(cell[0]*cell_size+left+cell_size//2,cell[1]*cell_size+top+cell_size//2),cell_size//2-2,1)
        self.k = True
        e.append(cell)

    def set_view(self, left, top, cell_size):
        pass
    def on_click(self, cell):
        b[cell[1]][cell[0]] = (b[cell[1]][cell[0]] + 1) % 2
        if self.k:
            self.cross(cell)
        else:
            self.criss(cell)
    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - left) // cell_size
        cell_y = (mouse_pos[1] - top) // cell_size
        if cell_x < 0 or cell_x >= width or cell_y < 0 or cell_y >= height:
            return None
        return cell_x, cell_y
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell in e:
            pass
        else:
            if cell:
                self.on_click(cell)   
    
board = Board(width, height)
running = True
board.render()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    #screen.fill((0, 0, 0))
    
    pygame.display.flip()
pygame.quit()
