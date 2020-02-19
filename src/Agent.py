#
#   Salvatore Campisi
#
#   A Star Pathfinding
#
#   February 2020, AA 19/20
#   Artificial Intelligence Laboratory
#

import numpy as np
import copy

# For managing the priority queue:
import heapq

class Agent():

    def __init__(self, grid):
        self.grid = grid

    def __grid_prep(self):
        labth = copy.deepcopy(self.grid.get())

        labth_rows, labth_cols = self.grid.get_dim()
        for r in range(labth_rows):
            for c in range(labth_cols):
                if(labth[r][c] == -1 or labth[r][c] == -2):
                    labth[r][c] = 1
                else:
                    labth[r][c] = 0
        return np.array(labth)

    def __heuristic(self, a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    def __a_star(self, labth, start, goal):
        neighbors_list = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

        # Dictionaries with the g and f score for each node:
        gscore = {start:0}
        fscore = {start:self.__heuristic(start, goal)}

        # Dictionary for storing the parent for each node in the path from start to goal:
        came_from = {}

        open_list = []
        close_set = set()

        heapq.heappush(open_list, (fscore[start], start) )

        while(open_list):

            # Popping the node with the lowest f score from the open list:
            current_node = heapq.heappop(open_list)[1]

            # Goal node is found:
            if(current_node == goal):

                # Generating the path:
                path_from_start_to_goal = []
                while(current_node in came_from):
                    path_from_start_to_goal.append(current_node)
                    current_node = came_from[current_node]

                return path_from_start_to_goal

            # If the current node is not the goal, add it to the close set:
            close_set.add(current_node)

            # Examining each neighbor of the current node:
            for i, j in neighbors_list:

                neighbor = current_node[0] + i, current_node[1] + j
                tentative_g_score = gscore[current_node] + self.__heuristic(current_node, neighbor)

                # Skip this iteration if neighbor is an obstacle or if is not inside the grid:
                if(0 <= neighbor[0] < labth.shape[0]):
                    if(0 <= neighbor[1] < labth.shape[1]):
                        if(labth[neighbor[0]][neighbor[1]] == 1):
                            continue
                    else:
                        continue
                else:
                    continue

                # Skip this iteration if the neighbor has already been visited AND is not possible to improve the g score:
                if(neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0)):
                    continue

                # If is it possible to improve the g score OR the neighbor is not already in the open list:
                if(tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_list]):
                    came_from[neighbor] = current_node
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.__heuristic(neighbor, goal)
                    heapq.heappush(open_list, (fscore[neighbor], neighbor))

        # There is no path from start to goal:
        return False

    def findpath_to_goal(self):
        start = (0,0)
        goal = self.grid.get_goal()
        labth = self.__grid_prep()

        path = self.__a_star(labth, start, goal)
        if(path == False):
            return False
        else:
            path = path + [start]
            path = path[::-1]
            return path
