from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def draw(drawing):
        pass
    def __init__(self) -> None:
        super().__init__()