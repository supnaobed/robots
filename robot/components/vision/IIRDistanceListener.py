import string
from abc import ABC, abstractmethod
from typing import Optional, List


class IIRDistanceListener(ABC):
    @abstractmethod
    def on_update_distance(self, distance: Optional[float]):
        pass


