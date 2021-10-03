from elements.element import Element


class Sprint(Element):

    # we use this list to write information
    # about year and quarter on the canvas
    list_sprints = list()

    X_OFF_SET = 15
    Y_OFF_SET = 50
    Y_ROW_SIZE = 25

    def __init__(self, x: int, y: int, width: int, year, quarter,
                 iteration: int, start, end) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.year = year
        self.quarter = quarter
        self.iteration = iteration
        self.start = start
        self.end = end
        self.elements = list()
        Sprint.list_sprints.append(self)

    def __str__(self):
        return f"Sprint {self.year}-{self.quarter}-{self.iteration}: " + \
               f"{self.start:%Y-%m-%d} to {self.end:%Y-%m-%d}"

    def contains(self, start, end):
        complete_in_sprint = (start >= self.start) & (end <= self.end)
        start_in_sprint = (start >= self.start) & (start <= self.end)
        end_in_sprint = (end >= self.start) & (end <= self.end)
        interrim = (start < self.start) & (end > self.end)
        return complete_in_sprint | start_in_sprint | end_in_sprint | interrim

    def getContentPoint(self):
        return (self.x, self.y)

    def addItem(self, element):

        x = self.x + Sprint.X_OFF_SET
        y = self.y + Sprint.Y_OFF_SET + Sprint.Y_ROW_SIZE * len(self.elements)
        element.setContentPoint(x, y)
        self.elements.append(element)

    def draw(self, dwg) -> None:
        dwg.add(dwg.line(start=(self.x, self.y),
                         end=(self.x, self.y+1080)))
        dwg.add(dwg.line(start=(self.x+self.width, self.y),
                         end=(self.x+self.width, self.y+1080)))
        dwg.add(dwg.text(text=f"Sprint {self.year}-Q{self.quarter}-{self.iteration}",
                         insert=(self.x + 10, self.y+20),
                         fill='black', font_size='12px', font_family="Arial"))
        for element in self.elements:
            element.draw(dwg)
