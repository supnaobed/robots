import time

from robot.components.controller.IRobotController import IRobotController
from data.RobotVision import RobotVision
from task.IAITask import IAITask, STATUS_COMPLETED, STATUS_PROCESS, calculate_angle

STATE_ARM_DOWN = 0
STATE_LURKING = 1
STATE_CATCHING = 2
STATE_ARM_UP = 3


class CatchTask(IAITask):
    _state = STATE_ARM_DOWN
    _is_move_arm: bool = False
    _start_time = 0

    def __init__(self,
                 controller: IRobotController,
                 movement_time_sec: float = 2.0,
                 angle_threshold: int = 5,
                 distance_threshold: float = 0.1):
        self.controller = controller
        self.movement_time_sec = movement_time_sec
        self.angle_threshold = angle_threshold
        self.distance_threshold = distance_threshold

    # TODO REFACTOR!
    def on_update_vision(self, vision: RobotVision) -> int:
        if vision.nearest_target is None:
            _state = STATE_ARM_UP
        if self._state == STATE_ARM_UP or self._state == STATE_ARM_DOWN:
            if self._is_move_arm:
                if time.time() - self._start_time < self.movement_time_sec:
                    self._is_move_arm = False
                    if self._state == STATE_ARM_UP:
                        return STATUS_COMPLETED
                    self._state = STATE_LURKING
            else:
                self._is_move_arm = True
                if self._state == STATE_ARM_UP:
                    self.controller.move_arm(200, 50)
                else:
                    self.controller.move_arm(200, -100)

        if self._state == STATE_LURKING:
            bias_angle = calculate_angle(vision, vision.nearest_target)
            if abs(bias_angle) > self.angle_threshold:
                self.controller.stop_move()
                self.controller.rotate(bias_angle)
            else:
                if vision.nearest_target.distance_in_meters <= self.distance_threshold:
                    self.controller.stop_move()
                    self._state = STATE_CATCHING
                else:
                    self.controller.move_forward(0.05)

        if self._state == STATE_CATCHING:
            self.controller.close_gripper()
            self._state = STATE_ARM_UP

        return STATUS_PROCESS
