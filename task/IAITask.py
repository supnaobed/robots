from abc import ABC, abstractmethod

from data.RobotVision import RobotVision
from data.WorldObject import WorldObject

STATUS_PROCESS = 0
STATUS_COMPLETED = 1


class IAITask(ABC):

    @abstractmethod
    def on_update_vision(self, vision: RobotVision) -> int:
        """
        :return status of completion. Use STATUS_PROCESS if completed
        """
        pass


def sign(value) -> float:
    if value == 0:
        return 0
    else:
        return abs(value) / value


def calculate_angle(vision: RobotVision,
                    world_object: WorldObject) -> float:
    vision_center_x = vision.vision_width / 2.0
    bias_x = (world_object.x + world_object.width / 2.0) - vision_center_x
    bias_angle = (bias_x / vision_center_x) * (vision.camera_angle / 2.0)
    return bias_angle

