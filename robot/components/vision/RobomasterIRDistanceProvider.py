from robomaster import sensor

from robot.components.vision import IIRDistanceListener


class RobomasterIRDistanceProvider:

    def __init__(self,
                 listener: IIRDistanceListener,
                 ep_robotic_sensor: sensor,
                 sensor_adaptor: sensor.SensorAdaptor):
        self.listener = listener
        self.ep_sensor_adaptor = sensor_adaptor
        self.adc = self.ep_sensor_adaptor.get_adc(id=1, port=1)

        self.ep_robotic_sensor = ep_robotic_sensor
        ep_robotic_sensor.sub_distance(freq=5, callback=self.sub_data_handler)

    def sub_data_handler(self, sub_info):
        print("sub_data_handler " + str(sub_info))
        self.listener.on_update_distance(sub_info[0]/1000)
