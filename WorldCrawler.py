import random
import time
from typing import Optional, List

from data.Command import Command
from data.CommandType import CommandType
from robot.components.controller.IRobotController import IRobotController
from world.RobotMapPosition import RobotMapPosition
from worldapi import IWorldCrawler


class WorldCrawler(IWorldCrawler):
    _move_command_distance = 0.5
    _move_command_time = _move_command_distance * 1.1
    _min_distance = 1
    _angle_step = 30
    _angle_threshold = 15

    _commands: List[Command] = []

    _command_start_time = 0

    def __init__(self,
                 robotMapPosition: RobotMapPosition,
                 controller: IRobotController):
        self._controller = controller
        self._robotMapPosition = robotMapPosition

    def get_commands(self) -> List[Command]:
        return self._commands

    def on_update_distance(self, distance: Optional[float]):
        print("distance " + str(distance))
        if time.time() - self._command_start_time < self._move_command_time:
            return

        if distance is None:
            distance = self._min_distance + 1

        self._command_start_time = time.time()
        if distance < self._min_distance:
            angle = random.randrange(self._angle_step - self._angle_threshold, self._angle_step - self._angle_threshold)
            self._robotMapPosition.add_obstacle_on_map(distance)
            command = Command(CommandType.ROTATE, angle)
            self._commands.append(command)
            self._controller.rotate(angle)
            self._robotMapPosition.move_robot_on_map(command)
        else:
            command = Command(CommandType.MOVE, self._move_command_distance)
            self._commands.append(command)
            self._controller.move_forward(self._move_command_distance)
            self._robotMapPosition.move_robot_on_map(command)
