from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def draw(drawing):
        pass

    def setContentPoint(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, range) -> None:
        super().__init__()
        self.x = None
        self.y = None
        self.range = range

    def get_range(self):
        return self.range
