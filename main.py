
from robomaster import robot
from RobotAI import RobotAI

from robot.components.controller.RobomasterController import RobomasterController


def setup_robot():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type='ap')
    controller = RobomasterController(
        ep_robot.chassis,
        ep_robot.robotic_arm,
        ep_robot.gripper
    )
    robot_ai = RobotAI(controller)



if __name__ == '__main__':
    setup_robot()
