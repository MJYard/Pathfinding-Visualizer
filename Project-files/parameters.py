import pygame
import pygame.freetype


pygame.freetype.init()

width =1000
height=1000
side_panel_width=500
rows = 100
columns = 100

rows_dict = {50:100, 100:200, 200:250, 250:500, 500:50}

hor_gap = width//rows
ver_gap = height//rows

game_font = pygame.freetype.SysFont('ariel', 14)
window=pygame.display.set_mode([width+side_panel_width,width])

state_toggle={'Menu':[], 'Pathfinding':[], 'Maze Generation':[]}
button_list =[]

    

