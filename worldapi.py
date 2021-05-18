from abc import ABC, abstractmethod
from typing import List

from data.Command import Command
from robot.components.vision.IIRDistanceListener import IIRDistanceListener


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
