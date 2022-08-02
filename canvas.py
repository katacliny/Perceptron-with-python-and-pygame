from dis import dis
from typing import List
import pygame as py
import random as r
from Perceptron.point import Point  # type: ignore
from Perceptron.perceptron import Perceptron  # type: ignore

# SUM = x0 * w0 + x1 * w1
# DIGN(N) if n > 0 -> 1 else -> -1
# Error = answer - guess

h: int = 400
w: int = 400

display: py.Surface = py.display.set_mode((h, w))
tiempo: py.time.Clock = py.time.Clock()

perceptron: Perceptron = Perceptron()
training_points: List[Point] = []
test_points: List[Point] = []
pos_y: int
pos_x: int
# create the points for train

for x in range(500):
    pos_y = r.randint(0, h)
    pos_x = r.randint(0, w)
    training_points.append(Point((pos_x, pos_y), display, train=True))

# end

# train the perceptron

for pt in training_points:
    perceptron.set_inputs(pt.pos)
    perceptron.train(pt.label)

# end

# create test points

for x in range(5):
    pos_y = r.randint(0, h)
    pos_x = r.randint(0, w)
    test_points.append(Point((pos_x, pos_y), display, train=False))

# end

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
    display.fill((255, 255, 255))
    py.draw.line(display, (0, 0, 0), (0, 0), (w, h))
    for p in test_points:
        # predict
        perceptron.set_inputs(p.pos)
        p.label = perceptron.guess()
        p.draw()
        # end
    tiempo.tick(60)
    py.display.update()
