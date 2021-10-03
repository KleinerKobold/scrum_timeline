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
    for index, row in dfs[1].iterrows():
        build_sprint(builder, index, row)

    for index, row in dfs[0].iterrows():
        build_an_item(index, row)
    builder.draw()

    print(dwg.tostring())
    dwg.save()
    logger.debug("Done")


def build_sprint(builder, index, row):
    print(row['Year'], row['Quarter'], row['Iteration'],
          row['Start'], row['End'])
    sprint = Sprint(200*index, 0, 200,
                    row['Year'], row['Quarter'], row['Iteration'],
                    row['Start'], row['End'])
    builder.add(sprint)


def build_an_item(index, row):
    x_off = 20
    y_off = 50
    print(row['Type'], row['Start'], row['Summary'])
    list_contents = list()
    for sprint in Sprint.list_sprints:
        start = row['Start']
        end = row['End']
        contains = sprint.contains(start, start if pd.isna(end) else end)
        if contains:
            list_contents.append(sprint)

        logger.debug(f"item \"{row['Summary']}\" at {start:%Y-%m-%d} " +
                     f"{'is' if contains else 'is not'} {sprint}")
    my_range = len(list_contents)
    if my_range > 0:
        item = Bonbon(x_off, (y_off+25*index), len(list_contents)*(150+(50 if my_range > 1 else 0)-50),
                      my_range, row['Summary'],
                      background=getBackground(row['Type']), )
        list_contents[0].addItem(item)


if __name__ == '__main__':
    main()
