from elements.element import Element


class Bonbon(Element):
    def __init__(self, x: int, y: int, width: int, 
                 title: str, background='blue', foreground='white') -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.title = title
        self.background = background
        self.foreground = foreground

    def draw(self, dwg):
        r = 10
        dwg.add(dwg.circle((self.x, self.y),
                           (r), fill=self.background))
        dwg.add(dwg.circle((self.x+self.width, self.y),
                           (r), fill=self.background))
        dwg.add(dwg.rect((self.x, self.y-r),
                         (self.width, r*2), fill=self.background))
        dwg.add(dwg.text(text=self.title,
                         insert=(self.x, self.y+3),
                         fill=self.foreground,
                         font_size='12px', font_family="Arial"))
    