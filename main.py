import pygame
from graph import Graph

pygame.init()

# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode(RESOLUTION)

# Init
## Graph properties
graph_width = 199
graph_height = 119
p = 0.52
graph = Graph(graph_width, graph_height, p)
percolation = graph.percolation()

## Visual properties
cell_width = 5
margin = 5
thickness = 2

def get_coord(x:int, y:int):
    return (cell_width*x + margin, cell_width*y + margin)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            graph = Graph(graph_width, graph_height, p)
            percolation = graph.percolation()

    screen.fill(BLACK)
    
    v = graph.vertical_connections
    for y in range(0, v.shape[0]):
        for x in range(0, v.shape[1]):
            if v[y,x] == 1:
                pygame.draw.line(screen, WHITE, get_coord(x,y), get_coord(x, y+1), thickness)

    h = graph.horizontal_connections
    for y in range(0, h.shape[0]):
        for x in range(0, h.shape[1]):
            if h[y,x] == 1:
                pygame.draw.line(screen, WHITE, get_coord(x,y), get_coord(x+1, y), thickness)

    if len(percolation) > 0:
        for i in range(0, len(percolation)-1):
            row1,col1 = percolation[i]
            row2,col2 = percolation[i+1]
            pygame.draw.line(screen, BLUE, get_coord(col1,row1), get_coord(col2,row2), thickness)
    
    pygame.display.flip()

pygame.quit()