import threading

from robomaster import chassis
from robomaster import gripper
from robomaster import robotic_arm

from robot.components.controller.IRobotController import IRobotController


class QueueRobomasterController(IRobotController):

    def __init__(self,
                 ep_chassis: chassis,
                 ep_robotic_arm: robotic_arm,
                 ep_robotic_gripper: gripper):
        self.controller = RobomasterController(ep_chassis, ep_robotic_arm, ep_robotic_gripper)
        self.threads = list()

    def move_forward(self, distance: float):
        self._join()
        t = threading.Thread(target=self.controller.move_forward, args=(distance,))
        t.start()

    def move_back(self, distance: float):
        self._join()
        t = threading.Thread(target=self.controller.move_back, args=(distance,))
        t.start()

    def move_left(self, distance: float):
        self._join()
        t = threading.Thread(target=self.controller.move_left, args=(distance,))
        t.start()

    def move_right(self, distance: float):
        self._join()
        t = threading.Thread(target=self.controller.move_right, args=(distance,))
        t.start()

    def stop_move(self):
        self._join()
        t = threading.Thread(target=self.controller.stop_move, args=())
        t.start()

    def rotate(self, angle: float):
        self._join()
        t = threading.Thread(target=self.controller.rotate, args=(angle,))
        t.start()

    def open_gripper(self):
        pass

    def close_gripper(self):
        pass

    def move_arm(self, x: int, y: int, sync: bool = True):
        pass

    def _join(self):
        for thread in self.threads:
            thread.join()


class RobomasterController(IRobotController):

    def __init__(self,
                 ep_chassis: chassis,
                 ep_robotic_arm: robotic_arm,
                 ep_gripper: gripper):
        self.ep_chassis = ep_chassis
        self.ep_robotic_arm = ep_robotic_arm
        self.ep_gripper = ep_gripper

    def move_forward(self, distance: float):
        self.ep_chassis.drive_speed(x=100, y=0, z=0, timeout=distance)
        # time.sleep(distance)
        print("move_forward")

    def move_back(self, distance: float):
        self.ep_chassis.drive_speed(x=-100, y=0, z=0, timeout=distance)
        # time.sleep(distance)

    def move_left(self, distance: float):
        self.ep_chassis.drive_speed(x=0, y=-100, z=0, timeout=distance)
        # time.sleep(distance)

    def move_right(self, distance: float):
        self.ep_chassis.drive_speed(x=0, y=100, z=0, timeout=distance)
        # time.sleep(distance)

    def stop_move(self):
        self.ep_chassis.drive_speed(x=0, y=0, z=0, timeout=1)
        # time.sleep(1)
        print("stop_move")

    def rotate(self, angle: float):
        timeout = 0.95 / 90 * abs(angle)
        self.ep_chassis.drive_speed(x=0, y=0, z=100 * sign(angle), timeout=timeout)
        # time.sleep(abs(timeout))
        print("rotate " + str(angle))

    def open_gripper(self):
        self.ep_gripper.open()

    def close_gripper(self):
        self.ep_gripper.close()

    def move_arm(self, x: int, y: int):
        try:
            self.ep_robotic_arm.moveto(x, y)
        except Exception:
            # TODO
            # Do Nothing!
            pass


def sign(value) -> float:
    if value == 0:
        return 0
    else:
        return abs(value) / value
