"""2D Vector data structure"""

from __future__ import annotations
from typing import NamedTuple
from math import dist


class Vec2D(NamedTuple):
    """2D vector point"""

    x: float
    y: float

    def distance_to(self, to_vec: Vec2D) -> float:
        """calc distance to another vector"""
        return dist(self, to_vec)

    def __repr__(self) -> str:
        return f"Vec2D({self.x=}, {self.y=})"

    def __add__(self, other: Vec2D) -> Vec2D:
        return Vec2D(self.x + other.x, self.y + other.y)
