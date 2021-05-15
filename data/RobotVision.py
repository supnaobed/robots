from dataclasses import dataclass, field
from typing import List, Optional

from data.WorldObject import WorldObject


def find_nearest(objects: List[WorldObject]) -> Optional[WorldObject]:
    if len(objects) == 0:
        return None
    nearest = objects[0]
    for i in objects:
        if i.distance_in_meters < nearest.distance_in_meters:
            nearest = i
    return nearest


def find_targets(objects: List[WorldObject]) -> List[WorldObject]:
    result: List[WorldObject] = []
    for i in objects:
        if i.is_target:
            result.append(i)
    return result


@dataclass
class RobotVision:
    world_objects: List[WorldObject] = field(default_factory=list)
    vision_width: int = 1920
    vision_height: int = 1080
    camera_angle: float = 120
    targets: List[WorldObject] = field(init=False)
    nearest_target: Optional[WorldObject] = field(init=False)

    def __post_init__(self):
        self.targets = find_targets(self.world_objects)
        self.nearest_target = find_nearest(self.targets)
