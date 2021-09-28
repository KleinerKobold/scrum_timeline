from elements.sprint import Sprint
import svgwrite
from read_excel import read_excel
from loguru import logger

from elements.bonbon import Bonbon
from elements.builder import Builder

def getBackground(type_name):
    if (type_name == 'Intervention'):
        return 'blue'
    if (type_name == 'Impediment'):
        return 'orange'
    raise("unkown type of row")

dfs = read_excel('events.xlsx')

dwg = svgwrite.Drawing('svgwrite-example.svg', profile='tiny')

builder = Builder(dwg)
for index,row in dfs[1].iterrows():
    print(row['Year'],row['Quarter'],row['Iteration'],row['Start'],row['End'])
    sprint = Sprint(200*index,0,200,row['Year'],row['Quarter'],row['Iteration'],row['Start'],row['End'])
    builder.add(sprint)

for index,row in dfs[0].iterrows():
    x_off = 20
    y_off = 50
    print(row['Type'],row['Start'],row['Summary'])
    builder.add(Bonbon(x_off,(y_off+25*index),150,row['Summary'],background=getBackground(row['Type'])))
builder.draw()


print(dwg.tostring())
dwg.save()
logger.debug("Done")