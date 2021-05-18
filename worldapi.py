import string
from abc import ABC, abstractmethod
from typing import Optional, List
from robot.components.vision.IIRDistanceListener import IIRDistanceListener
from data.Command import Command
from world import RobotMapPosition
from data import CommandType


class Point:
    x: float
    y: float

    def __init__(self, x, y):
        self.y = y
        self.x = x


class IWorldCrawler(IIRDistanceListener):

    @abstractmethod
    def get_commands(self) -> List[Command]:
        pass


class WorldCrawler(IWorldCrawler):

    def __init__(self,
                 robotMapPosition: RobotMapPosition):
        self.robotMapPosition = robotMapPosition

    def get_commands(self) -> List[Command]:
        pass

    def on_update_distance(self, distance: Optional[float]):
        if distance is not None:
            self.robotMapPosition.add_obstacle_on_map(distance.real)
            print("robot do some command")
            command = Command(CommandType.CommandType.MOVE, 1)
            self.robotMapPosition.move_robot_on_map(command)


class IMap(ABC):
    @abstractmethod
    def get_world_points(self) -> List[Point]:
        pass

    @abstractmethod
    def add_point(self, point: Point):
        pass

    @abstractmethod
    def add_vector(self, point: Point):
        pass

    #
    # @Danil! You must draw window with current map in real time
    #
