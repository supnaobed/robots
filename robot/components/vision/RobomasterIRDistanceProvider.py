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
        print("sensor adapter id1-port1 adc is {0}".format(self.adc))
        io = self.ep_sensor_adaptor.get_io(id=1, port=1)
        print("sensor adapter id1-port1 io is {0}".format(io))
        duration = self.ep_sensor_adaptor.get_pulse_period(id=1, port=1)
        print("sensor adapter id1-port1 duration is {0}ms".format(duration))
        self.listener.on_update_distance(sub_info[0])
