from typing import Optional

from robot.components.controller.IRobotController import IRobotController
from data.RobotVision import RobotVision
from data.WorldObject import WorldObject
from task.IAITask import IAITask, sign, STATUS_COMPLETED, STATUS_PROCESS


class FindTask(IAITask):
    _empty_frame_count = 0

    last_target: Optional[WorldObject] = None

    def __init__(self, controller: IRobotController):
        self.controller = controller

    def on_update_vision(self, vision: RobotVision) -> int:
        if len(vision.targets) > 0:
            self._empty_frame_count = 0
            return STATUS_COMPLETED
        if self._empty_frame_count > 50:
            self._empty_frame_count = 0
            target_center_x = 0
            if self.last_target is not None:
                target_center_x = self.last_target.x + self.last_target.width / 2
            if target_center_x == vision.vision_width / 2:
                target_center_x = 0
            self.controller.rotate(40 * sign(target_center_x - vision.vision_width / 2))
        else:
            self._empty_frame_count = self._empty_frame_count + 1
            self.controller.stop_move()
        return STATUS_PROCESS
