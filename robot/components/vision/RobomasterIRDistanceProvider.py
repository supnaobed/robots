from robomaster import sensor

from robot.components.vision import IIRDistanceListener


class RobomasterIRDistanceProvider:

    def __init__(self,
                 listener: IIRDistanceListener,
                 ep_robotic_sensor: sensor):
        self.listener = listener
        self.ep_robotic_sensor = ep_robotic_sensor
        ep_robotic_sensor.sub_distance(freq=5, callback=sub_data_handler, args=self)


def sub_data_handler(sub_info, distance_provider):
    if sub_info[0] < 1.0:
        distance_provider.listener.on_update_distance(sub_info[0])
    else:
        distance_provider.listener.on_update_distance(None)
