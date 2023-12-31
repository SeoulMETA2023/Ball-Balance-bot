"""Bot status data structure"""

from __future__ import annotations

from typing import Optional
from queue import Queue
import time

from core.plate import PlateController
from model.vector import Vec2D


class BotStatus:
    """Bot Status Data"""

    def __init__(
        self,
        timestamp: float,
        ball_pos: Vec2D,
        servo_x: int,
        servo_y: int,
    ) -> None:
        self.timestamp = timestamp
        self.ball_pos = ball_pos
        self.x_axis = servo_x
        self.y_axis = servo_y

    @classmethod
    def make(cls, ball_pos: Vec2D, plate: "PlateController") -> BotStatus:
        """make BotStatus automatically"""
        timestamp = time.time()
        return cls(timestamp, ball_pos, plate.servo_x.angle, plate.servo_y.angle)

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "ball_pos": self.ball_pos,
            "x_axis": self.x_axis,
            "y_axis": self.y_axis,
        }

    def __repr__(self) -> str:
        return (
            f"BotStatus("
            f"{self.timestamp=}, "
            f"{self.ball_pos=}, "
            f"{self.x_axis=}, "
            f"{self.y_axis=})"
        )


class BotStatusQueue(Queue):
    """Bot Status Queue"""

    def put(
        self, item: BotStatus, block: bool = True, timeout: float | None = None
    ) -> None:
        if not isinstance(item, BotStatus):
            raise ValueError("item should be BotStatus")
        return super().put(item, block, timeout)

    def get(
        self, block: bool = True, timeout: float | None = None
    ) -> Optional[BotStatus]:
        if self.full():
            return super().get(block, timeout)
        return None
