from queue import PriorityQueue
import grid
import node
import parameters
import pygame
import time
import buttons

def reconstruct_path(previous_node, node_path, end, g_score, start_var='Start'):
        path_list=[]
        path_length = g_score[end]
        path_length_text =f'Path Length: {round(path_length,1)}'     
        while True:
            if previous_node.check(start_var):
                break
            path_list.append(previous_node)
            previous_node.make_type('Route')
            grid.grid_update(previous_node)
            time.sleep(0.01)        
            previous_node=node_path[previous_node]
            #time.sleep(1)
            pygame.event.pump()
        return path_length_text

def Heuristic1(node,End,D=1):
    
    dx=abs(End.row-node.row)
    dy=abs(End.column-node.column)
    return D * (dx**2+dy**2)**0.5

def Heuristic2(node,End,D=10):
    dx=abs(End.row-node.row)
    dy=abs(End.column-node.column)
    return D**2 * (dx**2+dy**2)**5

def Heuristic3(node,End,D=1):
    
    dx=abs(End.row-node.row)
    dy=abs(End.column-node.column)
    return dx+dy



    


def AStar_alg(start, end, main_grid ,alg_type='Astar'):

    count = 0
    node_checked_count = 0
    node_list=PriorityQueue()
    node_set = {start}
    node_path={}
    f_score = {nodes: float('inf') for row in main_grid for nodes in row}
    g_score = {nodes: float('inf') for row in main_grid for nodes in row}
   
    f_score[start] = Heuristic3(start, end)
    g_score[start]=0
    previous_node=None
    node_score = (f_score[start], count,  start, previous_node)
    node_list.put(node_score)
    Flag = False

    while not Flag:       
        current = node_list.get()[2]       
        for neighbour_tuple in current.check_neighbours(main_grid):
            pygame.event.pump()
            #time.sleep(0.001)
            neighbour = neighbour_tuple[0]    
            temp_g_score = g_score[current] + neighbour.weight
            if temp_g_score < g_score[neighbour]:
                node_path[neighbour] = current
                g_score[neighbour] = temp_g_score

                a , b = 1, 1
                if alg_type == 'dijkstra':
                    a, b = 1, 0
                elif alg_type == 'greedy bfs':
                    a, b = 0, 1
                f_score[neighbour] =  a * temp_g_score + b * Heuristic1(neighbour, end)

                if neighbour not in node_set:
                    count += 1
                    node_set.add(neighbour)
                    node_score = (f_score[neighbour], count, neighbour, previous_node)
                    node_list.put(node_score)
                    if neighbour.check('End'):
                        Flag = True
                        break
                    neighbour.make_type('Open')
                    grid.grid_update(neighbour)
                    node_checked_count += 1

        if Flag:
            path_length_text = reconstruct_path(current, node_path, end, g_score)
            break

        if current != start:
            current.make_type('Closed', int(f_score[neighbour]))
            grid.grid_update(current)

    return path_length_text, node_checked_count

        
