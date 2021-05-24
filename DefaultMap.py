from typing import List
import numpy as np
import time

from matplotlib import pyplot as plt

from worldapi import IMap, Point


class DefaultMap(IMap):

    fig = plt.figure()
    plt.axis([0, 100, 0, 100])
    path = list()

    def get_world_points(self) -> List[Point]:
        pass

    def add_point(self, point: Point):
        plt.scatter(point.x, point.y)
        plt.pause(0.0001)

    def add_vector(self, point: Point):
        self.path.append(point)
        xs = [point.x for point in self.path]
        ys = [point.y for point in self.path]
        plt.plot(xs, ys, '.r-')
        plt.pause(0.0001)


if __name__ == '__main__':
    map = DefaultMap()
    for i in range(100):
        time.sleep(1)
        y = np.random.random() * 100
        map.add_point(Point(i, y))
        y2 = np.random.random() * 100
        x = np.random.random() * 100
        map.add_vector(Point(x, y2))
