import svgwrite

def bonbon(x : int, y:int, width:int, title:str, dwg, background='blue', foreground='white'):
    r= 10
    dwg.add(dwg.circle((x,y),(r),fill=background))
    dwg.add(dwg.circle((x+width,y),(r),fill=background))
    dwg.add(dwg.rect((x, y-r), (width,r*2),fill=background))
    dwg.add(dwg.text(text=title,insert=(x,y+3),
        fill=foreground, font_size='12px', font_family="Arial"))
    