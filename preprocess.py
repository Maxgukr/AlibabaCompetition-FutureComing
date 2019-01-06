import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from collections import defaultdict
import pickle

def load_city_data(path):

    node = []
    cnt=0
    with open(path,'r') as fr:
        for line in fr:
            cnt += 1
            lines = line.split(',')
            if cnt>1:
                node.append([int(lines[1]), int(lines[2])])

    node = np.array(node)
    return node.T


def load_weather_data_true(path):
    #grid = np.zeros((548, 421))
    #date = [1,2,3,4,5] # datetime
    hour = [i for i in range(3,21,1)]
    id = [(1,j) for j in hour]
    #weather_grid = {}
    walls = defaultdict(list)
    #for i in id:
        #for j in hour:
        #weather_grid[i] = np.zeros((548,421))
    #    walls[i] = []


    with open(path,'r') as fr:
        for line in fr:
            lines = line.split(',')
            #x.append(int(lines[0]))
            #y.append(int(lines[1]))
            #if lines[2]=='1' and lines[3]=='3': # first read one date one hour data for test
            if lines[2] == '1': # one day data
                if float(lines[4])>15.0:
                    #weather_grid[(int(lines[2]),int(lines[3]))][int(lines[0])-1][int(lines[1])-1] = 1 # 坠毁区域
                    walls[(int(lines[2]),int(lines[3]))].append((int(lines[0])-1,int(lines[1])-1))

            #if lines[0] == '548':
             #   break
    for i in id:
        walls[i] = set(walls[i])

    #fw1 = open('./preliminary/weather_data', 'w')
    #pickle.dump(weather_grid, fw1)

    return walls #,weather_grid,


def draw(road_path, point):
    #x=[i for i in range(548)]
    #y=[j for j in range(421)]


    #plt.contour(x,y,grid,1)
    #plt.imshow(grid)
    plt.scatter(point[0][0], point[1][0], c='r', s=14)
    plt.scatter(point[0][1:len(point[0])], point[1][1:len(point[1])], c='g', s=14)

    for key in road_path:
        plt.plot(road_path[key][0],road_path[key][1],'b-')
    plt.show()


def draw_grid(grid, point):
    for key in grid.keys():
        plt.scatter(point[0][0], point[1][0], c='r', s=14)
        plt.scatter(point[0][1:len(point[0])], point[1][1:len(point[1])], c='g', s=14)
        plt.imshow(grid[key].T, vmin=0, vmax=1, cmap='Greys')
        #fr = open('./img/'+str(key[0])+'-'+str(key[1]),'w')
        #img.imsave(fr, grid[key].T, vmax=1, vmin=0, cmap='Greys')
        #plt.show()
        plt.savefig(str(key[0])+str(key[1]))




class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        results = list(results)
        return results


