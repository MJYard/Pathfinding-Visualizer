import colours
import node
import mazes
import algorithms3
import grid
import saving
import parameters as pr
import buttons
import weights

import pygame
import itertools

def main():
    pygame.init()

    pr.window.fill(colours.Colours.white)
    main_grid = grid.Grid()
    grid.Draw(main_grid)

    start=None
    end=None
    running = True
    path_length = f'N/A'

   

    #Pathfinding
    pathfinding_title = buttons.Title('Pathfinding Algorithms', 'Titles', 1150, 20, 200, 30)

    astar_button = buttons.Toggle('A star', 'Pathfinding',
        *buttons.button_group_placement(1, pathfinding_title))
    dijkstra_button = buttons.Toggle('Dijkstra', 'Pathfinding',
        *buttons.button_group_placement(2,  pathfinding_title))
    #bi_astar_button = buttons.Toggle('Bidirectional Astar', 'Pathfinding',
        #*buttons.button_group_placement(3,  pathfinding_title))
    greedy_button = buttons.Toggle('Greedy BFS', 'Pathfinding',
     *buttons.button_group_placement(4,  pathfinding_title))

    #Mazes
    maze_title = buttons.Title('Mazes', 'Titles', 1150, 200, 200, 30)

    maze1_button = buttons.Toggle('Breadth First Search', 'Maze',
        *buttons.button_group_placement(1, maze_title))
    maze2_button = buttons.Toggle('Iterative backtracking', 'Maze',
        *buttons.button_group_placement(2, maze_title))
    maze3_button = buttons.Toggle('Breadth First Search (M)', 'Maze',
        *buttons.button_group_placement(3, maze_title))
    maze4_button = buttons.Toggle('maze4', 'Maze',
        *buttons.button_group_placement(4, maze_title))

    #Weights
    weight_title = buttons.Title('Node weights', 'Titles', 1150, 380, 200, 30)

    random_weight_button = buttons.Toggle('Random Weights', 'Weights',
        *buttons.button_group_placement(1,  weight_title))
    weight2_button = buttons.Toggle('weight2', 'Weights',
        *buttons.button_group_placement(2,  weight_title))
    #weight3_button = buttons.Toggle('weight3', 'Weights',
        #*buttons.button_group_placement(3,  weight_title))
    #weight4_button = buttons.Toggle('weight4', 'Weights',
        #*buttons.button_group_placement(4,  weight_title))

    #Menu
    menu_title = buttons.Title('Menu', 'Titles', 1150, 500, 200, 30)

    start_button = buttons.Switch('Start (Space)', 'Menu',
        *buttons.button_group_placement(1, menu_title))
    clear_button = buttons.Switch('Clear (C)', 'Menu',
        *buttons.button_group_placement(2, menu_title))
    reset_button = buttons.Switch('Reset (R)', 'Menu',
        *buttons.button_group_placement(3, menu_title))
    maze_button = buttons.Switch('Generate Maze (M)', 'Menu',
        *buttons.button_group_placement(4, menu_title))
    reset_weights_button = buttons.Switch('Reset Weights (W)', 'Menu',
        *buttons.button_group_placement(5, menu_title))
    turn_weighting_button = buttons.Switch('Turn weighting (T)', 'Menu',
        *buttons.button_group_placement(6, menu_title))
    
    #Results
    result_title = buttons.Title('Results', 'Titles', 1150, 740, 200, 30)

    path_length_button = buttons.Label(f'Path Length: {path_length}', 'Results',
        *buttons.button_group_placement(1, result_title))
    nodes_checked_button = buttons.Switch('result2', 'Nodes Checked: ',
        *buttons.button_group_placement(2, result_title))
  
    pygame.display.flip()

    while running:

        for event in pygame.event.get():

            if pygame.mouse.get_pressed():
                x,y = pygame.mouse.get_pos()
                i,j = grid.clicked_position(x,y)
                clicked_in_grid = grid.click_in_grid()

            key_pressed = event.type == pygame.KEYDOWN

            if event.type == pygame.QUIT or (key_pressed and event.key == pygame.K_ESCAPE):
                    running = False
                    print('Exited')

            elif (key_pressed and event.key == pygame.K_SPACE or start_button.is_clicked()) and (start and end):
                
                start_button.clicked_button()
                if astar_button.is_clicked():
                    results = algorithms3.AStar_alg(start, end, main_grid, alg_type='Astar')

                elif dijkstra_button.is_clicked():
                    results = algorithms3.AStar_alg(start, end, main_grid, alg_type='dijkstra')

                elif greedy_button.is_clicked():
                    results = algorithms3.AStar_alg(start, end, main_grid, alg_type='greedy bfs')

                #elif bi_astar_button.is_clicked():
                    #results = algorithms3.bi_Astar(start, end, main_grid)
                    
                else:
                    dijkstra_button.toggle_state()
                    results = algorithms3.AStar_alg(start, end, main_grid, alg_type='dijkstra')


                nodes_checked_button.change_name(f'Nodes Checked: {results[1]}')
                path_length_button.change_name(results[0])

                start_button.unclick_button()
           


            elif key_pressed and event.key == pygame.K_m or maze_button.is_clicked():

                maze_button.clicked_button()
                if maze1_button.is_clicked():
                    start, end = mazes.Breadth_first_search(main_grid, modified=False)

                elif maze2_button.is_clicked():
                    start, end = mazes.iter_backtracking(main_grid)

                elif maze3_button.is_clicked():
                    start, end = mazes.Breadth_first_search(main_grid, modified=True)

                else:
                    maze1_button.toggle_state()
                    mazes.Breadth_first_search(main_grid, modified=False)

                maze_button.unclick_button()

            
                
            elif  random_weight_button.is_clicked():
                weights.random_weights(main_grid)
                random_weight_button.unclick_button()

            elif weight2_button.is_clicked():
                
                pr.rows = pr.rows_dict[pr.rows]
                pr.columns = pr.rows
                pr.hor_gap = pr.width//pr.rows
                pr.ver_gap = pr.height//pr.rows
                main_grid = grid.Grid()
                grid.Draw(main_grid)
                start = None
                end = None
                weight2_button.unclick_button()



            

            

            elif key_pressed and event.key == pygame.K_c or clear_button.is_clicked():
                clear_button.is_clicked()
                start,end = grid.grid_clear(main_grid)
                clear_button.unclick_button()

            elif key_pressed and event.key == pygame.K_r or reset_button.is_clicked():
                reset_button.is_clicked()
                grid.grid_reset(main_grid)
                reset_button.unclick_button()

            elif key_pressed and event.key == pygame.K_w or reset_weights_button.is_clicked():
                reset_weights_button.is_clicked()
                weights.reset_weights(main_grid)
                reset_weights_button.unclick_button()



                    


            elif clicked_in_grid:

                if pygame.mouse.get_pressed()[0] and not start:
                    main_grid[i,j].make_type('Start')
                    grid.grid_update(main_grid[i,j])
                    start=main_grid[i,j]

                elif pygame.mouse.get_pressed()[0] and start and not end:
                    if not main_grid[i,j].check('Start'):
                        main_grid[i,j].make_type('End')
                        grid.grid_update(main_grid[i,j])
                        end=main_grid[i,j]

                elif pygame.mouse.get_pressed()[0] and start and end:
                    if main_grid[i,j].check('Path'):
                        main_grid[i,j].make_type('Barrier')
                        grid.grid_update(main_grid[i,j])

                elif pygame.mouse.get_pressed()[2]:
                    if main_grid[i,j].check('Start'):
                        start=None
                    elif main_grid[i,j].check('End'):
                        end=None
                    main_grid[i,j].make_type('Path')
                    grid.grid_update(main_grid[i,j])

            for button in [x for lst in pr.state_toggle.values() for x in lst]:
                if button.rectangle.collidepoint(x,y):
                    if pygame.mouse.get_pressed()[0]:
                        button.toggle_state()


            

if __name__ == '__main__':
    main()
