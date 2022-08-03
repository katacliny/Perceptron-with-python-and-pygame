import random as r
from typing import List
from abstractions import APerceptron


class Perceptron(APerceptron):
    def __init__(self, inputs: tuple[float, float, float] = (0, 0, 0)):
        self.possible_weights: tuple[float, float] = (-1, 1)
        self.weights: List[float] = [
            r.choice(self.possible_weights),
            r.choice(self.possible_weights),
            r.choice(self.possible_weights),
        ]
        self.inputs: tuple[float, float, float] = inputs
        self.lr: float = 0.1

    def set_inputs(self, inputs: tuple[float, float, float]) -> None:
        self.inputs = inputs

    def sign(self, n: float) -> int:
        if n > 0:
            return 1
        else:
            return -1

    def guess(self) -> int:
        return self.sign(
            (self.weights[0] * self.inputs[0])
            + (self.weights[1] * self.inputs[1])
            + (self.weights[2] * self.inputs[2])
        )

    def train(self, target: int) -> None:

        guess: int = self.guess()
        error: int = target - guess

        for i, w in enumerate(self.weights):
            self.weights[i] += error * self.inputs[i] * self.lr
