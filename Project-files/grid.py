import parameters as pr
import numpy as np
import node
import pygame
import colours

# Core grid functionality

def Grid():
    print(pr.rows)
    grid = np.zeros([pr.rows,pr.columns], dtype=object)
    for i in range(pr.rows):
        for j in range(pr.columns):
            grid[i,j]=node.Node(i,j)
            grid[i,j].make_type('Path')
    return grid

def Display_grid():
    grid_visual = np.zeros([pr.rows,pr.columns], dtype=object)
    for i in range(pr.rows):
        for j in range(pr.columns):
            grid_visual[i][j]=grid[i][j].grid_vis
    return grid_visual

def Draw_grid(Grid):

    for i in range(pr.rows + 1):
        pygame.draw.line(pr.window, colours.Colours.grey, (0, i * pr.ver_gap), (pr.columns * pr.hor_gap, i * pr.ver_gap))
    for j in range(pr.columns + 1):
        pygame.draw.line(pr.window, colours.Colours.grey, (j * pr.hor_gap, 0), (j * pr.hor_gap, pr.rows * pr.ver_gap))

def Draw(Grid):
    #The main drawing function win.fill() fills the entire screenin one colour every frame. Not efficient, but fine for this purpose.
    Draw_grid(Grid)
    for row in Grid:
        for node in row:
            node.draw_node()

    pygame.display.update()

def grid_update(Node):
    grid_node = (Node.y_pos+1, Node.x_pos+1, Node.hor_gap-1, Node.ver_gap-1)
    Node.draw_node()
    pygame.display.update(grid_node)

def full_grid_update():
    rect=(0, 0, pr.width, pr.height)
    pygame.display.update(rect)

def clicked_position(x_pos, y_pos):
    row=x_pos//pr.hor_gap
    column=y_pos//pr.ver_gap
    return row,column

def click_in_grid():
    if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
        x,y = pygame.mouse.get_pos()
        if x+1 <=pr.width and y+1 <=pr.height:
            return True

def grid_reset(main_grid):
    for i in range(pr.rows):
        for j in range(pr.columns):
            if not main_grid[i,j].check("Barrier") and not main_grid[i,j].check("Start") and not main_grid[i,j].check("End"):
                main_grid[i,j].make_type('Path')
                grid_update(main_grid[i,j])

def grid_clear(main_grid):
    for i in range(pr.rows):
        for j in range(pr.columns):
            main_grid[i,j].make_type('Path')
            grid_update(main_grid[i,j])
    start=None
    end=None
    return start, end


# grid clicking 

