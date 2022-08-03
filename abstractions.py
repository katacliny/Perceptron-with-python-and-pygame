from abc import ABC, abstractmethod


class APerceptron(ABC):
    @abstractmethod
    def set_inputs(self, inputs: tuple[float, float, float]) -> None:
        """"""

    @abstractmethod
    def sign(self, n: float) -> int:
        """"""

    @abstractmethod
    def guess(self) -> int:
        """"""

    @abstractmethod
    def train(self, target: int) -> None:
        """"""


class APoint(ABC):
    @abstractmethod
    def draw(self) -> None:
        """"""

    @abstractmethod
    def get_translated_pos(self) -> tuple[int, int]:
        """"""
