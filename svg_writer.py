import svgwrite
from loguru import logger
dwg = svgwrite.Drawing('svgwrite-example.svg', profile='tiny')

def bonbon(x : int, y:int, width:int, title:str, dwg):
    r= 10
    dwg.add(dwg.circle((x,y),(r),fill='blue'))
    dwg.add(dwg.circle((x+width,y),(r),fill='blue'))
    dwg.add(dwg.rect((x, y-r), (width,r*2),fill='blue'))
    dwg.add(dwg.text(text=title,insert=(x,y+3),
    fill='white',
    font_size='12px',
    font_family="Courier New"))
    

bonbon(20,20,100,"Test",dwg)

bonbon(60,60,150,"test",dwg)


print(dwg.tostring())
dwg.save()
logger.debug("Done")