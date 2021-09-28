from elements.element import Element

class Builder:
    def __init__(self,drawing) -> None:
        self.elements = list()
        self.drawing = drawing
        pass
    def add(self, item:Element):
        self.elements.append(item)
    def draw(self):
        for item in self.elements:
            item.draw(self.drawing)