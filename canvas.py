from audioop import bias
from dis import dis
from typing import List
import pygame as py
import random as r
from point import Point  # type: ignore
from perceptron import Perceptron  # type: ignore
from settings import h, w
from utils import f

# SUM = x0 * w0 + x1 * w1
# DIGN(N) if n > 0 -> 1 else -> -1
# Error = answer - guess

display: py.Surface = py.display.set_mode((h, w))
tiempo: py.time.Clock = py.time.Clock()

perceptron: Perceptron = Perceptron()
training_points: List[Point] = []
test_points: List[Point] = []
pos_y: float
pos_x: float
# create the points for train


for x in range(500):
    pos_y = r.uniform(-1, 1)
    pos_x = r.uniform(-1, 1)
    training_points.append(Point((pos_x, pos_y), display, train=True))

# end

# train the perceptron

for pt in training_points:
    perceptron.set_inputs((*pt.pos, pt.bias))
    perceptron.train(pt.label)

# end

# create test points

for x in range(25):
    pos_y = r.uniform(-1, 1)
    pos_x = r.uniform(-1, 1)
    test_points.append(Point((pos_x, pos_y), display, train=False))

# end

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
    display.fill((255, 255, 255))
    # py.draw.line(display, (0, 0, 0), (0, h), (w, 0))
    p1: Point = Point((-1, f(-1)), display)
    p2: Point = Point((1, f(1)), display)

    py.draw.aaline(display, (0, 0, 0), p1.get_translated_pos(), p2.get_translated_pos())
    for p in test_points:
        # predict
        perceptron.set_inputs((*p.pos, p.bias))
        p.label = perceptron.guess()
        p.draw()
        # end
    tiempo.tick(60)
    py.display.update()
