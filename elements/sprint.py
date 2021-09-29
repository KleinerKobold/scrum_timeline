from elements.element import Element


class Sprint(Element):

    # we use this list to write information
    # about year and quarter on the canvas
    list_sprints = list()

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
        Sprint.list_sprints.append(self)

    def __str__(self):
        return f"Sprint {self.year}-{self.quarter}-{self.iteration}: " + \
               f"{self.start:%Y-%m-%d} to {self.end:%Y-%m-%d}"

    def contains(self, start, end):
        return (start >= self.start) & (end <= self.end)

    def getContentPoint(self):
        return (self.x, self.y)

    def draw(self, dwg) -> None:
        dwg.add(dwg.line(start=(self.x, self.y),
                         end=(self.x, self.y+1080)))
        dwg.add(dwg.line(start=(self.x+self.width, self.y),
                         end=(self.x+self.width, self.y+1080)))
        dwg.add(dwg.text(text=f"Sprint {self.iteration}",
                         insert=(self.x + 10, self.y+20),
                         fill='black', font_size='12px', font_family="Arial"))
