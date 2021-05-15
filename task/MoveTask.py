from robot.components.controller.IRobotController import IRobotController
from data.RobotVision import RobotVision
from data.WorldObject import WorldObject
from task.IAITask import IAITask, calculate_angle, STATUS_COMPLETED, STATUS_PROCESS

STATUS_LOST_TARGET = 2


class MoveTask(IAITask):

    def __init__(self, controller: IRobotController,
                 angle_threshold: float = 20.0,
                 distance_threshold: float = 1.0,
                 angle_step: float = 3.0):
        self.controller = controller
        self.angle_threshold = angle_threshold
        self.distance_threshold = distance_threshold
        self.angle_step = angle_step

    def on_update_vision(self, vision: RobotVision) -> int:
        nearest: WorldObject = vision.nearest_target
        if nearest is None:
            self.controller.stop_move()
            return STATUS_LOST_TARGET
        bias_angle = calculate_angle(vision, nearest)
        if abs(bias_angle) > self.angle_threshold:
            self.controller.stop_move()
            self.controller.rotate(bias_angle)
        else:
            if nearest.distance_in_meters <= self.distance_threshold:
                self.controller.stop_move()
                return STATUS_COMPLETED
            else:
                self.controller.move_forward(1000)
        return STATUS_PROCESS
