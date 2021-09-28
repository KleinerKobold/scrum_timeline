import svgwrite
from loguru import logger

from forms.bonbon import bonbon
dwg = svgwrite.Drawing('svgwrite-example.svg', profile='tiny')

bonbon(20,20,100,"Test",dwg)

bonbon(60,60,150,"test",dwg)


print(dwg.tostring())
dwg.save()
logger.debug("Done")