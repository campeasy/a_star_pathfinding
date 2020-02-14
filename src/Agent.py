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
        neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        close_set = set()
        came_from = {}

        # Dictionaries with the g and f score for each node:
        gscore = {start:0}
        fscore = {start:self.__heuristic(start, goal)}

        oheap = []
        heapq.heappush(oheap, (fscore[start], start))

        while oheap:
            current = heapq.heappop(oheap)[1]

            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data

            close_set.add(current)

            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + self.__heuristic(current, neighbor)

                if 0 <= neighbor[0] < labth.shape[0]:
                    if 0 <= neighbor[1] < labth.shape[1]:
                        if labth[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue

                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.__heuristic(neighbor, goal)
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))
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
