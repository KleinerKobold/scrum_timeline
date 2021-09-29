from elements.sprint import Sprint
import svgwrite
from read_excel import read_excel
from loguru import logger
import pandas as pd


from elements.bonbon import Bonbon
from elements.builder import Builder
from util import getBackground

def main():
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
        for sprint in Sprint.list_sprints:
            start = row['Start']
            end = row['End']
            contains = sprint.contains(start, start if pd.isna(end) else end)
            logger.debug(f"item {row['Summary']} at {start:%Y-%m-%d} {'is' if contains else 'is not'} {sprint}")
        builder.add(Bonbon(x_off,(y_off+25*index),150,row['Summary'],background=getBackground(row['Type'])))
    builder.draw()


    print(dwg.tostring())
    dwg.save()
    logger.debug("Done")

if __name__ == '__main__':
    main()