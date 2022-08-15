import parameters as pr
import pygame
import colours
import random
import pygame.gfxdraw
import numpy as np



class Node:

    def __init__(self, row, column,  node_type='Node', default_colour=True, *node_colour):
        self.node_type = node_type
        self.node_colour = node_colour
        self.default_colour = default_colour
        self.row = row
        self.column = column
        self.hor_gap = pr.hor_gap
        self.ver_gap = pr.ver_gap
        self.x_pos = column * pr.hor_gap
        self.y_pos = row * pr.ver_gap
        self.weight = 1
        #self.lr_weight = 1
        #self.ud_weight = 1
        self.direction = None
        self.grid_vis = node_type[0]
        #self.visited = False
        self.visit = 0
        

    def __str__(self):
        return str((self.node_type, self.row, self.column))

    def __repr__(self):
        return str((self.node_type, self.row, self.column))

    def __lt__(self, other):
        return self

    def grid_rep(self):
        return self.grid_vis

    def check_type(self):
        return self.node_type

    def check(self, type_name):
        return type_name.title() == self.node_type

    def draw_node(self):
       
        return pygame.gfxdraw.box(pr.window, 
            (self.row * self.hor_gap + 1, self.column * self.ver_gap + 1,
                self.hor_gap - 1, self.ver_gap - 1),self.node_colour,)


    def set_weight(self, value):
        self.weight=value
        if self.check('Path'):
            self.node_colour=(255,255-self.weight*8,255-self.weight*8)
            self.draw_node()

    def make_type(self, type_name, var=0):
        match type_name.title():

            case 'Path':
                self.node_type = 'Path'
                self.direction = None

                if self.default_colour:
                    self.node_colour = (255,255-self.weight*8,255-self.weight*8)

            case 'Barrier':
                self.node_type = 'Barrier'

                if self.default_colour:
                    self.node_colour = colours.Colours.black

            case 'Open':
                self.node_type = 'Open'

                if self.default_colour:
                   
                    self.node_colour = pygame.Color(0,0,255,100)

            case 'Closed':
                self.node_type = 'Closed'

                if self.default_colour:
                    if var:
                        scale1=((var)/(var+(pr.rows*np.sqrt(2))/4))*255
                        scale2=((var)/(var+(pr.rows*np.sqrt(2))))*255
                        scale3=((var)/(var+pr.rows**2)/(pr.rows/10))*255
            
                        self.node_colour=(scale2,255-scale3,scale1,100)

                    else:
                        self.node_colour = colours.Colours.green

            case 'Open1':
                self.node_type = 'Open1'

                if self.default_colour:
                    self.node_colour = pygame.Color(0,0,255,50)

            case 'Closed1':
                self.node_type = 'Closed1'

                if self.default_colour:
                    self.node_colour = pygame.Color(0,255,0,50)

            case 'Open2':
                self.node_type = 'Open2'

                if self.default_colour:
                    self.node_colour = colours.Colours.blue

            case 'Closed2':
                self.node_type = 'Closed2'

                if self.default_colour:
                    self.node_colour = colours.Colours.green

            case 'Route':
                self.node_type = 'Route'

                if self.default_colour:
                    self.node_colour = colours.Colours.light_salmon

            case 'Start':
                self.node_type = 'Start'

                if self.default_colour:
                    self.node_colour = colours.Colours.orange

            case 'End':
                self.node_type = 'End'

                if self.default_colour:
                    self.node_colour = colours.Colours.red

            case _:
                print('Error: Unregognised Node type. Type set to: Node')
                self.node_type = 'Node'

        self.grid_vis = self.node_type[0]
        self.draw_node()

    def check_neighbours(self,grid):
        neighbors_list=[]

        if self.row != pr.rows-1: 
            if not grid[self.row+1,self.column].check('Barrier'): #Right
                neighbors_list.append((grid[self.row+1,self.column],'right'))

        if self.column != 0:
            if not grid[self.row,self.column-1].check('Barrier') : #Up
                neighbors_list.append((grid[self.row,self.column-1],'up'))

        if self.column != pr.columns-1:
            if not grid[self.row,self.column+1].check('Barrier') : #Down
                neighbors_list.append((grid[self.row,self.column+1],'down'))
                
                
        if self.row != 0:
            if not grid[self.row-1,self.column].check('Barrier') : #Left
                neighbors_list.append((grid[self.row-1,self.column],'left'))
                

       
               

        return neighbors_list

    def check_neighbors_breadth_path(self,main_grid,Rows,Columns, c=0):
        neighbors_list=[]

        if self.row != (Rows-1 or Rows-1): 
            if  main_grid[self.row+2,self.column].visit < random.choices([1,2],[20,c],k=1)[0]: #Right
                neighbors_list.append(main_grid[self.row+2,self.column])
                main_grid[self.row+2,self.column].visit+=1
                main_grid[self.row+1,self.column].make_type('Path')
                
        if self.row >1:
            if  main_grid[self.row-2,self.column].visit < random.choices([1,2],[20,c],k=1)[0] : #Left
                neighbors_list.append(main_grid[self.row-2,self.column])
                main_grid[self.row-2,self.column].visit+=1
                main_grid[self.row-1,self.column].make_type('Path')
            
        if self.column != (Columns-1 or Columns-1):
            if  main_grid[self.row,self.column+2].visit  < random.choices([1,2],[20,c],k=1)[0] : #Down
                neighbors_list.append(main_grid[self.row,self.column+2])
                main_grid[self.row,self.column+2].visit+=1
                main_grid[self.row,self.column+1].make_type('Path')
                
        if self.column >1 :
            if main_grid[self.row,self.column-2].visit  < random.choices([1,2],[20,c],k=1)[0]: #Up
                neighbors_list.append(main_grid[self.row,self.column-2])
                main_grid[self.row,self.column-2].visit+=1
                main_grid[self.row,self.column-1].make_type('Path')

        return neighbors_list

    def check_neighbors_recursive(self,main_grid,Rows,Columns, c=0):
        neighbors_list=[]
        

        if self.row != (Rows-1 or Rows-1): 
            if  main_grid[self.row+2,self.column].visit < 1: #Right
                neighbors_list.append((main_grid[self.row+2,self.column],main_grid[self.row+1,self.column], self))
                #main_grid[self.row+2,self.column].visit+=1
                
                
        if self.row >1:
            if  main_grid[self.row-2,self.column].visit < 1: #Left
                neighbors_list.append((main_grid[self.row-2,self.column],main_grid[self.row-1,self.column]))
                #main_grid[self.row-2,self.column].visit+=1
                
            
        if self.column != (Columns-1 or Columns-1):
            if  main_grid[self.row,self.column+2].visit  < 1: #Down
                neighbors_list.append((main_grid[self.row,self.column+2],main_grid[self.row,self.column+1]))
                #main_grid[self.row,self.column+2].visit+=1
               
                
        if self.column >1 :
            if main_grid[self.row,self.column-2].visit  < 1: #Up
                neighbors_list.append((main_grid[self.row,self.column-2],main_grid[self.row,self.column-1]))
                #main_grid[self.row,self.column-2].visit+=1
                

      


        return neighbors_list
