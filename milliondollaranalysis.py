#! python3
#Author: Joe DeFilippo

import milliondollardata as mdd
import pprint
from PIL import Image, ImageDraw


def countSitesWithStatusCode(mdhpData, sc):
    totalSites = len(mdhpData) + 1
    count = 0
    for i in range(1, totalSites):
        if mdhpData[i]['status'] == sc:
            count += 1
    return count

def statusCodeSummary(mdhpData):
    count = {}
    totalSites = len(mdhpData) + 1

    for i in range(1, totalSites):
        count[mdhpData[i]['status']] = 0
    for i in range(1, totalSites):
        count[mdhpData[i]['status']] += 1

    return count

def generateHeatmap(mdhpData):
    im = Image.new('RGBA', (1000, 1000), 'white')
    draw = ImageDraw.Draw(im)

    totalSites = len(mdhpData) + 1

    for i in range(1, totalSites):
        if mdhpData[i]['status'] == 0:
            draw.rectangle(eval(mdd.millionDollarData[i]['coords']), fill='blue')
        elif mdhpData[i]['status'] == 200:
            draw.rectangle(eval(mdd.millionDollarData[i]['coords']), fill='green')
        else:
            draw.rectangle(eval(mdd.millionDollarData[i]['coords']), fill='red')
    im.save('heatmap.png')

x = mdd.millionDollarData

print(countSitesWithStatusCode(x, 200))
print(pprint.pformat(statusCodeSummary(x)))


generateHeatmap(x)
