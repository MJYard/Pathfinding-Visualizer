import parameters as pr
import random
import grid
import numpy as np

def reset_weights(main_grid):
	for row in main_grid:
		for node in row:
			node.set_weight(1)
			grid.grid_update(node)

def random_weights(main_grid):
	print(pr.rows)
	for row in main_grid:
		for node in row:
			node.set_weight(random.uniform(1,10))
			grid.grid_update(node)

def wave_noise(main_grid):
	print(1)
	
	



