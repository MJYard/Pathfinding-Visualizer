import parameters as pr
import grid
import random
import pygame
import time
import sys 

sys.setrecursionlimit(2500000)

def Breadth_first_search(main_grid, modified=True):

	start = None
	end = None

	choice_list_Row=[]
	choice_list_Column=[]
	Node_list=[]

	for rows in main_grid:
		for node in rows:
			node.make_type('Barrier')
			node.visit=0
			node.draw_node()

	for i in range(1,pr.rows,2):
		choice_list_Row.append(i)

		for j in range(1,pr.columns,2):
			main_grid[i,j].make_type('Path')
			main_grid[i,j].draw_node()


	for j in range(1,pr.columns-1,2):
		choice_list_Column.append(j)
	Start_node=main_grid[random.choice(choice_list_Row),random.choice(choice_list_Column)]
	Node_list.append(Start_node)
	Start_node.draw_node()
	grid.full_grid_update()
	

	while Node_list:

		random.shuffle(Node_list)
		current=Node_list[0]
		if modified:
			c=1
		else:
			c=0
	
		current_iter = current.check_neighbors_breadth_path(main_grid,pr.rows,pr.columns,c)
		
		for i in current_iter:
			Node_list.append(i)
			grid.grid_update(i)
			grid.grid_update(main_grid[i.row,i.column-1])
			time.sleep(0.001)
			if i.column <pr.columns-1:
				grid.grid_update(main_grid[i.row,i.column+1])
			grid.grid_update(main_grid[i.row-1,i.column])
			if i.row <pr.rows-1:
				grid.grid_update(main_grid[i.row+1,i.column])
			pygame.event.pump()
						

		Node_list.remove(current)
	return start, end


def recursive_backtracking(main_grid):
	
	start = None
	end = None

	choice_list_Row=[]
	choice_list_Column=[]
	Node_list=[]
	visited_nodes={}

	for rows in main_grid:
		for node in rows:
			node.make_type('Barrier')
			node.visit=0
			node.draw_node()

	for i in range(1,pr.rows,2):
		choice_list_Row.append(i)

		for j in range(1,pr.columns,2):
			main_grid[i,j].make_type('Path')
			main_grid[i,j].draw_node()

	for j in range(1,pr.columns-2,2):
		choice_list_Column.append(j)
	Start_node=main_grid[random.choice(choice_list_Row),random.choice(choice_list_Column)]
	#Node_list.append(Start_node)
	Start_node.draw_node()
	grid.full_grid_update()
	print(Start_node)
	flag=False
	

	def temp_func(current, flag):
		
		current_iter = current.check_neighbors_recursive(main_grid,pr.rows,pr.columns)
		
		

		for i in current_iter:
			Node_list.append(i[0])
			visited_nodes[i[0]]=current

		if current_iter:
			if flag:
				barrier_row = (visited_nodes[current].row - current.row)/2
				barrier_column = (visited_nodes[current].column - current.column)/2 
				barrier_break = (int(current.row+barrier_row),int(current.column+barrier_column))
				connected_node = main_grid[barrier_break[0], barrier_break[1]]
				connected_node.make_type('Path')
				grid.grid_update(connected_node)
				
			flag=False   
			connected_node=random.choice(current_iter)
			connected_node[0].visit+=1
			
			Node_list.remove(connected_node[0])
			
			break_path = connected_node[1]
			break_path.make_type("Path")
			grid.grid_update(break_path)
			
			time.sleep(0.2)
			pygame.event.pump()
			
			temp_func(connected_node[0], flag)
		else:
			flag=True
			Node_list.remove(Node_list[-1])
			pygame.event.pump()
			if not Node_list:
				return None
			temp_func(Node_list[-1], flag)
		



	temp_func(Start_node, flag)


def iter_backtracking(main_grid):

	def temp_func(current, flag):
	
		current_iter = current.check_neighbors_recursive(main_grid,pr.rows,pr.columns)
		
		

		for i in current_iter:
			Node_list.append(i[0])
			visited_nodes[i[0]]=current

		if current_iter:
			if flag:
				barrier_row = (visited_nodes[current].row - current.row)/2
				barrier_column = (visited_nodes[current].column - current.column)/2 
				barrier_break = (int(current.row+barrier_row),int(current.column+barrier_column))
				connected_node = main_grid[barrier_break[0], barrier_break[1]]
				connected_node.make_type('Path')
				grid.grid_update(connected_node)
				
			flag=False   
			connected_node=random.choice(current_iter)
			connected_node[0].visit+=1
			grid.grid_update(connected_node[0])
			
			Node_list.remove(connected_node[0])
			
			break_path = connected_node[1]
			break_path.make_type("Path")
			grid.grid_update(break_path)
			pygame.event.pump()
			
			time.sleep(0.001)
			
			temp_func(connected_node[0], flag)

	start = None
	end = None
	loop_flag = True

	choice_list_Row=[]
	choice_list_Column=[]
	Node_list=[]
	visited_nodes={}

	for rows in main_grid:
		for node in rows:
			node.make_type('Barrier')
			node.visit=0
			node.draw_node()

	for i in range(1,pr.rows,2):
		choice_list_Row.append(i)

		for j in range(1,pr.columns,2):
			main_grid[i,j].make_type('Path')
			main_grid[i,j].draw_node()

	for j in range(1,pr.columns-2,2):
		choice_list_Column.append(j)
	Start_node=main_grid[random.choice(choice_list_Row),random.choice(choice_list_Column)]
	#Node_list.append(Start_node)
	Start_node.draw_node()
	grid.full_grid_update()
	
	flag=False
	temp_func(Start_node, flag)
	while loop_flag:
		
		
		flag=True
		Node_list.remove(Node_list[-1])
	
		if not Node_list:
			loop_flag = False

			break
		temp_func(Node_list[-1], flag)
		#Node_list[-1].visit=True
	return start, end

