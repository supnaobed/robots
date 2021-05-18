from data.CommandType import CommandType
from worldapi import IMap
from worldapi import Point
from data import Command
import math


def get_point(distance: float, angle: float):
    x = math.cos(angle) * distance
    y = math.sin(angle) * distance
    return Point(x, y)


class RobotMapPosition:
    robotPosition = Point(0, 0)
    robotAngle = 0.0

    def __init__(self,
                 robotMap: IMap):
        self.robotMap = robotMap
        self.update_map(Point(0, 0), angle=0)

    def update_map(self, point: Point, angle: float):
        self.robotPosition = point
        self.robotAngle = angle
        self.robotMap.add_vector(point)

    def add_obstacle_on_map(self, distance: float):
        self.robotMap.add_point(get_point(distance, angle=self.robotAngle))

    def move_robot_on_map(self, command: Command):
        if command.commandType == CommandType.MOVE:
            self.update_map(get_point(command.value, self.robotAngle), angle=self.robotAngle)
        if command.commandType == CommandType.MOVE:
            self.update_map(self.robotPosition, angle=command.value)
