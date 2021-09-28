import svgwrite
from read_excel import read_excel
from loguru import logger

from elements.bonbon import Bonbon
from elements.builder import Builder

dfs = read_excel('events.xlsx')

dwg = svgwrite.Drawing('svgwrite-example.svg', profile='tiny')

builder = Builder(dwg)
for index,row in dfs[1].iterrows():
    print(row['Year'],row['Quarter'],row['Iteration'],row['Start'],row['End'])

for index,row in dfs[0].iterrows():
    x_off = 20
    y_off = 20
    print(row['Type'],row['Start'],row['Summary'])
    background = None
    if (row['Type'] == 'Intervention'):
        background = 'blue'
    if (row['Type'] == 'Impediment'):
        background='orange'
    builder.add(Bonbon(x_off,(y_off+25*index),150,row['Summary'],background=background))
builder.draw()


print(dwg.tostring())
dwg.save()
logger.debug("Done")