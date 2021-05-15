from robot.components.controller.IRobotController import IRobotController
from robot.components.vision.IRobotVisionListener import IRobotVisionListener
from data.RobotVision import RobotVision
from task.CatchTask import CatchTask
from task.FindTask import FindTask
from task.IAITask import IAITask, STATUS_COMPLETED
from task.InitTask import InitTask
from task.MoveTask import MoveTask, STATUS_LOST_TARGET


class RobotAI(IRobotVisionListener):

    def __init__(self,
                 controller: IRobotController):
        self.controller = controller

        self.find_task = FindTask(controller)
        self.move_task = MoveTask(controller)
        self.catch_task = CatchTask(controller)

        self.current_task: IAITask = InitTask(controller)

    def on_update_vision(self, vision: RobotVision):
        if self.current_task is InitTask:
            code = self.current_task.on_update_vision(vision)
            if code == STATUS_COMPLETED:
                self.current_task = self.find_task
        if self.current_task is FindTask:
            code = self.current_task.on_update_vision(vision)
            if code == STATUS_COMPLETED:
                self.current_task = self.move_task
        if self.current_task is MoveTask:
            code = self.current_task.on_update_vision(vision)
            if code == STATUS_COMPLETED:
                self.current_task = self.catch_task
            elif code == STATUS_LOST_TARGET:
                self.current_task = self.find_task

        if self.current_task is CatchTask:
            code = self.current_task.on_update_vision(vision)
            # TODO Move back

        if vision.nearest_target is not None:
            self.find_task.last_target = vision.nearest_target
