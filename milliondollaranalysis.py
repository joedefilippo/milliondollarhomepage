#! python3
#Author: Joe DeFilippo

import milliondollardata as mdd
import pprint
from PIL import Image, ImageDraw
from collections import Counter


def countSitesWithStatusCode(mdhpData, sc):
    count = 0
    for i in range(1, len(mdhpData) + 1):
        if mdhpData[i]['status'] == sc:
            count += 1
    return count

def getStatusCodeSummary(mdhpData):
    count = {}
    for i in range(1, len(mdhpData) + 1):
        count[mdhpData[i]['status']] = 0
    for i in range(1, len(mdhpData) + 1):
        count[mdhpData[i]['status']] += 1
    return count

def getStatusCodeSummaryCounter(mdhpData):
    #TODO find better way here
    result = Counter(mdhpData.values())
    return result

def generateHeatmap(mdhpData):
    im = Image.new('RGBA', (1000, 1000), 'white')
    draw = ImageDraw.Draw(im)

    for i in range(1, len(mdhpData) + 1):
        if mdhpData[i]['status'] == 0:
            draw.rectangle(eval(mdd.millionDollarData[i]['coords']), fill='blue')
        elif mdhpData[i]['status'] == 200:
            draw.rectangle(eval(mdd.millionDollarData[i]['coords']), fill='green')
        else:
            draw.rectangle(eval(mdd.millionDollarData[i]['coords']), fill='red')
    im.save('heatmap.png')

def getSitesOffline(mdhpData):
    for i in range(1, len(mdhpData) + 1):
        if mdhpData[i]['status'] != 0:
            del mdhpData[i]
    return mdhpData

def getSitesPendingOrder(mdhpData):
    for i in range(1, len(mdhpData) + 1):
        if mdhpData[i]['title'].lower() != 'pending order':
            del mdhpData[i]
    return mdhpData

def getSitesReserved(mdhpData):
    for i in range(1, len(mdhpData) + 1):
        if 'reserved' not in mdhpData[i]['title'].lower():
            del mdhpData[i]
    return mdhpData

def getSitesPendingOrderOrReserved(mdhpData):
    return {**getSitesPendingOrder(mdhpData.copy()),**getSitesReserved(mdhpData)}


x = mdd.millionDollarData

#print(countSitesWithStatusCode(x, 200))
#print(pprint.pformat(statusCodeSummary(x)))

#generateHeatmap(x)
#print(pprint.pformat(getSitesReserved(x)))
#print(pprint.pformat(getSitesPendingOrder(x)))

#TODO
# print(pprint.pformat(getStatusCodeSummaryCounter(x)))

print(pprint.pformat(getSitesPendingOrderOrReserved(x)))