import svgwrite
from read_excel import read_excel
from loguru import logger

from elements.bonbon import Bonbon
from elements.builder import Builder

dfs = read_excel('events.xlsx')

dwg = svgwrite.Drawing('svgwrite-example.svg', profile='tiny')

builder = Builder(dwg)
for index,row in dfs[0].iterrows():
    x_off = 20
    y_off = 20
    print(row['Type'],row['Start'],row['Summary'])
    if (row['Type'] == 'Intervention'):
        builder.add(Bonbon(x_off,(y_off+25*index),150,row['Summary']))
    elif (row['Type'] == 'Impediment'):
        builder.add(Bonbon(x_off,(y_off+25*index),150,row['Summary'],background='orange'))
builder.draw()


print(dwg.tostring())
dwg.save()
logger.debug("Done")