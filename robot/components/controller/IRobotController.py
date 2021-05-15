from abc import abstractmethod, ABC
from typing import Optional


class IRobotController(ABC):
    @abstractmethod
    def move_forward(self, distance: Optional[float]):
        pass

    @abstractmethod
    def move_back(self, distance: float):
        pass

    @abstractmethod
    def move_left(self, distance: float):
        pass

    @abstractmethod
    def move_right(self, distance: float):
        pass

    @abstractmethod
    def stop_move(self):
        pass

    @abstractmethod
    def rotate(self, angle: float):
        pass

    @abstractmethod
    def open_gripper(self):
        pass

    @abstractmethod
    def close_gripper(self):
        pass

    @abstractmethod
    def move_arm(self, x: int, y: int):
        pass
