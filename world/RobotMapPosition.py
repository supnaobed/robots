from data.CommandType import CommandType
from worldapi import IMap
from worldapi import Point
from data import Command
import math


def get_point(distance: float, angle: float):
    x = math.cos(math.radians(angle)) * distance
    y = math.sin(math.radians(angle)) * distance
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
        # print("point: " + str(point.x) + " " + str(point.y))

    def add_obstacle_on_map(self, distance: float):
        point = get_point(distance, angle=self.robotAngle)
        point.x = point.x + self.robotPosition.x
        point.y = point.y + self.robotPosition.y
        self.robotMap.add_point(point)

    def move_robot_on_map(self, command: Command):
        if command.commandType == CommandType.MOVE:
            old_point = self.robotPosition
            delta = get_point(command.value, self.robotAngle)
            new_point = Point(old_point.x + delta.x, old_point.y + delta.y)
            self.update_map(new_point, angle=self.robotAngle)
        if command.commandType == CommandType.ROTATE:
            self.robotAngle = command.value
