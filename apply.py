from preprocess import *
from path_find import *


def path_search(point, walls):
    '''
    find path for 10 goals from 3:00 to 21:00 clock
    :param weather_grid: dict each time weather condition
    :param point: start and goals
    :param walls: region with winds >= 15
    :return: path for each goal
    '''
    start_init = (point[0][0], point[1][0])
    end = [(point[0][i], point[1][i]) for i in range(1,11,1)]
    path_goals = {} # record path for each goal
    #for p in end:
     #   path_goals[p] = []

    sg = SquareGrid(width=421, height=548)
    sg_all = {}
    for id in walls.keys():
        sg_all[id] = sg
        sg_all[id].walls = walls[id] # grid for each time slice

    frontier = PriorityQueue() # priority queue
    frontier.put(start_init,0) # first point push queue
    came_from = {} # record path
    cost_so_far = {} # record cost
    came_from[start_init] = None
    cost_so_far[start_init] = 0
    start = start_init
    #cnt = 0
    #for i in range(len(end)): # for each goal
    for id in sg_all.keys():
    #cnt += 1
        came_from, cost_so_far, current, frontier = A_star(sg_all[id],start,end=end[7],
                                             came_from=came_from, cost_so_far=cost_so_far, frontier=frontier)
        if current != end[7] and id == (1,20):
            print(end[7])
            path_goals[end[7]] = reconstruct_path(came_from=came_from, start=start_init, end=current)

        if current != end[7] and id != (1,20):
            start = current
            came_from = came_from
            cost_so_far = cost_so_far
            frontier = frontier
    #elif current != end[i]:
    #   print(end[i],"no path has been found!")

        elif current == end[7]: # change another goal
        #cnt = 0
            path_goals[end[7]] = reconstruct_path(came_from=came_from, start=start_init, end=end[7])
            start = start_init
            came_from = {}
            cost_so_far = {}
            came_from[start_init] = None
            cost_so_far[start_init] = 0
            frontier = PriorityQueue()  # priority queue
            frontier.put(start_init, 0)  # first point push queue
            break

    return path_goals






def main():
    path1 = './preliminary/In_situMeasurementforTraining_201712.csv'
    walls= load_weather_data_true(path1)

    path2 = './CityData.csv'
    point = load_city_data(path2)



    #came_from, came_so_far, current = A_star(sg, start=start, end=end)

    #road_path = reconstruct_path(came_from, start=start, end=current)
    #draw_grid(grid, road_path)

    road_path = path_search(point=point, walls=walls)

    draw(point=point, road_path=road_path)
    #draw_grid(weather_grid, point)

if __name__ == "__main__":
    main()