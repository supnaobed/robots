from robomaster import robot

from DefaultMap import DefaultMap
from WorldCrawler import WorldCrawler
from robot.components.controller.RobomasterController import RobomasterController
from robot.components.vision.RobomasterIRDistanceProvider import RobomasterIRDistanceProvider
from world.RobotMapPosition import RobotMapPosition


def setup_robot():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type='ap')
    controller = RobomasterController(
        ep_robot.chassis,
        ep_robot.robotic_arm,
        ep_robot.gripper
    )
    map_position = RobotMapPosition(DefaultMap())

    crawler = WorldCrawler(map_position, controller)
    distance_provider = RobomasterIRDistanceProvider(crawler, ep_robot.sensor)


if __name__ == '__main__':
    setup_robot()
