from typing import List
import numpy as np
import time

from matplotlib import pyplot as plt

from worldapi import IMap, Point


class DefaultMap(IMap):
    fig = plt.figure()
    plt.axis([-10, 10, -10, 10])
    path = list()
    points = list()

    def get_world_points(self) -> List[Point]:
        pass

    def add_point(self, point: Point):
        self.points.append(point)

    def add_vector(self, point: Point):
        self.path.append(point)

    def run(self):
        while True:
            plt.clf()
            for point in self.points:
                plt.scatter(point.x, point.y)
            xs = [point.x for point in self.path]
            ys = [point.y for point in self.path]
            plt.plot(xs, ys, '.r-')
            plt.pause(0.001)


if __name__ == '__main__':
    map = DefaultMap()
    map.add_point(Point(2, 3))
    map.add_point(Point(4, 32))
    map.add_point(Point(8, 84))
    map.add_point(Point(55, 90))
    map.add_point(Point(24, 11))
    map.run()

