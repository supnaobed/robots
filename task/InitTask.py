from robot.components.controller.IRobotController import IRobotController
from data.RobotVision import RobotVision
from task.IAITask import IAITask, STATUS_COMPLETED, STATUS_PROCESS
import time


class InitTask(IAITask):
    _start_time = 0
    _is_move: bool = False

    def __init__(self, controller: IRobotController,
                 movement_time_sec: float = 1.5):
        self.controller = controller
        self.movement_time_sec = movement_time_sec

    def on_update_vision(self, vision: RobotVision) -> int:
        if not self._is_move:
            self.controller.open_gripper()
            self.controller.move_arm(200, 50)
            self._is_move = True
            self._start_time = time.time()
        else:
            if time.time() - self._start_time > self.movement_time_sec:
                return STATUS_COMPLETED
        return STATUS_PROCESS
