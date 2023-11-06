"""Find Ball in array image"""

from __future__ import annotations
from typing import Sequence

import numpy

from model.vector import Vec2D


class BallFinder:
    """Detect Ball in 3D array image"""

    def __init__(self, lower: Sequence[int], upper: Sequence[int]) -> None:
        self.lower = numpy.array(lower)
        self.upper = numpy.array(upper)

    @classmethod
    def from_config(cls) -> BallFinder:
        from config.config import get_config

        config = get_config()
        lower = config["detector"]["lower"]
        upper = config["detector"]["upper"]

        return cls(lower, upper)

    def find_pos(self, arr_image: numpy.ndarray) -> Vec2D:
        """calc the position of the ball using the array image"""
        x_arr, y_arr = numpy.where(((self.lower <= arr_image) & (arr_image <= self.upper)).all(axis=2))

        if x_arr.size:
            return Vec2D(numpy.average(x_arr), numpy.average(y_arr))

        raise BallNotFoundError


class BallNotFoundError(Exception):
    pass
