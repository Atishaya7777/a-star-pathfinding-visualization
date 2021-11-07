import pygame
import math
from queue import PriorityQueue

WIDTH = 800
# Create a width * width display window
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path finding algorithm visualized")

# Colors
# Note: the color will determine what state that particular node is in. If it is red, it is closed, green then it is open, black then is an obstacle, orange is it is the path and so on.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        # Note: the color determines whether the node is in the closed list or in the open list. Obviously, the color red defines that the node is in the closed list 
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == PURPLE

    def is_reset(self):
        return self.color == WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color = BLACK
    
    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = PURPLE
    
    def make_reset(self):
        self.color = WHITE

    def draw(self, window):
        # pygame.draw.rect(window, <some value> , (positionX, positionY, width, height))
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        # comeback to this later as this is a big function
        pass

    # Less than == lt
    def __lt__(self, other):
        return False

# Heuristic function
def h_cost(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)

def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width))

def draw(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(window)

    draw_grid(window, rows, width)

    pygame.display.update()

def get_clicked_pos(position, rows, width):
    gap = width // rows
    y, x = position

    row = y // gap
    col = x // gap


def main(window, width):
    # Try changing these static values to dynamic later on
    ROWS = 50
    grid = make_grid(ROWS, width)
    
    start = None
    end = None

    run = True
    started = False
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue

            # mouse.get_pressed()[0] is the left hand side of the mouse and mouse.get_pressed()[2] is the right hand side button of the mouse.
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = get_clicked_pos(position, ROWS, WIDTH)
                node = grid[row][col]

                

    pygame.quit()
