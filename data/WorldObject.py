from dataclasses import dataclass


@dataclass
class WorldObject:
    x: int = 0
    y: int = 0
    width: int = 0
    height: int = 0
    distance_in_meters: float = 0.0
    is_target: bool = False
