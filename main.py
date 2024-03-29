from robomaster import robot
from data.Command import Command
from data.CommandType import CommandType
import math

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
    map = DefaultMap()
    map_position = RobotMapPosition(map)
    crawler = WorldCrawler(map_position, controller)
    distance_provider = RobomasterIRDistanceProvider(crawler,
                                                     ep_robot.sensor,
                                                     ep_robot.sensor_adaptor)
    map.run()


if __name__ == '__main__':
    setup_robot()
    # map = DefaultMap()
    # map_position = RobotMapPosition(map)
    # map_position.move_robot_on_map(Command(CommandType.MOVE, 1.0))
    # map_position.move_robot_on_map(Command(CommandType.ROTATE, 180.0))
    # map_position.move_robot_on_map(Command(CommandType.MOVE, 1.0))


# import robomaster
# from robomaster import robot
# import time
#
#
# def sub_data_handler(sub_info):
#     distance = sub_info
#     print("tof1:{0}  tof2:{1}  tof3:{2}  tof4:{3}".format(distance[0], distance[1], distance[2], distance[3]))
#
#
# if __name__ == '__main__':
#     ep_robot = robot.Robot()
#     ep_robot.initialize(conn_type="ap")
#
#     ep_sensor = ep_robot.sensor
#     ep_sensor.sub_distance(freq=5, callback=sub_data_handler)
#     time.sleep(60)
#     ep_sensor.unsub_distance()
#     ep_robot.close()
