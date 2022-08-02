import pygame as py
from abstractions import APoint  # type: ignore


class Point(APoint):
    def __init__(self, pos: tuple[int, int], dipsplay: py.Surface, train: bool = False) -> None:
        self.pos: tuple[int, int] = pos
        self.display: py.surface = dipsplay
        self.label: int = (1 if self.pos[0] > self.pos[1] else -1) if train else 0

    def draw(self) -> None:
        color: tuple[int, int, int] = (250, 0, 0) if self.label == 1 else (0, 255, 0)
        py.draw.circle(self.display, color, self.pos, radius=5)
