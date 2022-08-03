import pygame as py
from abstractions import APoint  # type: ignore
from settings import h, w
from utils import f


def translate(value: float, leftMin: int, leftMax: int, rightMin: int, rightMax: int) -> float:
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def pos_x(x: float) -> int:
    return int(translate(x, -1, 1, 0, w))


def pos_y(y: float) -> int:
    return int(translate(y, -1, 1, h, 0))


class Point(APoint):
    def __init__(self, pos: tuple[float, float], dipsplay: py.Surface, train: bool = False) -> None:
        self.pos: tuple[float, float] = pos
        self.display: py.surface = dipsplay
        line_y: float = f(self.pos[0])
        self.label: int = (1 if self.pos[1] > line_y else -1) if train else 0

    def draw(self) -> None:
        color: tuple[int, int, int] = (250, 0, 0) if self.label == 1 else (0, 255, 0)
        py.draw.circle(self.display, color, (pos_x(self.pos[0]), pos_y(self.pos[1])), radius=5)

    def get_translated_pos(self) -> tuple[int, int]:

        return (pos_x(self.pos[0]), pos_y(self.pos[1]))
