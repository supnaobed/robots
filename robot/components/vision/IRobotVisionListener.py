from abc import abstractmethod, ABC

from data.RobotVision import RobotVision


class IRobotVisionListener(ABC):
    @abstractmethod
    def on_update_vision(self, vision: RobotVision):
        pass
