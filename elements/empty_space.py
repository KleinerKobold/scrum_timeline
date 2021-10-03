from elements.element import Element


class Empty_Space(Element):
    def __init__(self, x: int, y: int, width: int) -> None:
        super().__init__(range)
        self.x = x
        self.y = y
        self.width = width

    def draw(self, dwg):
        pass
