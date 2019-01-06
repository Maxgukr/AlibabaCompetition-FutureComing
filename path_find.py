import numpy as np
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1-x2) + abs(y1-y2)


def A_star(grid, start, end, came_from, cost_so_far, frontier): # start and end are tuple
    '''

    :param grid:
    :param start:
    :param end:
    :param came_from:
    :param cost_so_far:
    :return:
    '''
    #frontier = PriorityQueue() # priority queue
    #frontier.put(start,0) # first point push queue
    #came_from = {} # record path
    #cost_so_far = {} # record cost
    #came_from[start] = None
    #cost_so_far[start] = 0
    cnt = 0
    wait = 0
    current = ()
    next = ()
    while not frontier.empty():
        prio, current = frontier.get()
        cnt += 1
        #print(current)
        if current == end:
            break

        if len(grid.neighbors(current)) >1: # can find reasonal dirc
            for next in grid.neighbors(current): # 判断可能的几个方向, 需要包含往回退的情况。
                #if next != came_from[current]: # 不往回走
                new_cost = cost_so_far[current] + 1 # 所有的权重都是１
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = heuristic(next, end)
                    frontier.put(next, priority)
                    came_from[next] = current
                #else:
                    #came_from[next] = came_from[current] # 往回走
        else:
            wait += 1
            frontier.put(current, prio) # can't find stay here, push back, maybe stay for an hour
            next = current
            print('wait times:', wait)


        if cnt == 30: # every hour at most 30 steps
            current = next
            break

    return came_from, cost_so_far, current, frontier


def reconstruct_path(came_from, start, end):
    current = end
    path = []
    while current != start:
        path.append([current[0], current[1]])
        current = came_from[current]
    path.append([start[0], start[1]])
    path.reverse()

    path = np.array(path)

    return path.T