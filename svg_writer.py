import svgwrite
from loguru import logger
dwg = svgwrite.Drawing('svgwrite-example.svg', profile='tiny')

def bonbon(x : int, y:int, width:int, dwg):
    r= 10
    dwg.add(dwg.circle((x,y),(r),fill='blue'))
    dwg.add(dwg.circle((x+width,y),(r),fill='blue'))
    dwg.add(dwg.rect((x, y-r), (width,r*2),fill='blue'))
bonbon(20,20,100,dwg)

bonbon(40,50,150,dwg)


print(dwg.tostring())
dwg.save()
logger.debug("Done")