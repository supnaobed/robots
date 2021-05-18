from typing import List

from matplotlib import pyplot as plt

from worldapi import IMap, Point


class DefaultMap(IMap):
    points: List[Point] = []
    path: List[Point] = []

    def get_world_points(self) -> List[Point]:
        pass

    def add_point(self, point: Point):
        self.points.append(point)
        self.draw()

    def add_vector(self, point: Point):
        self.path.append(point)
        self.draw()

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        x_points = list()
        y_points = list()
        for point in self.points:
            x_points.append(point.x)
            y_points.append(point.y)

        ax.plot(x_points, y_points, 'b')

        x_points_path = list()
        y_points_path = list()
        # for point in self.path:
        #     x_points_path.append(point.x)
        #     y_points_path.append(point.y)
        #
        # ax.plot(x_points_path, y_points_path, 'r')

        ax.set_xlabel('x-points')
        ax.set_ylabel('y-points')
        fig.show()
        plt.pause(3)