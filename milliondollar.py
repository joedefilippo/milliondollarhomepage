#! python3
#Author: Joe DeFilippo

# In 2005, Alex Tew, a student from England, developed a web page to help pay for his university education
# The Million Dollar Homepage (milliondollarhomepage.com) was born.  The webpage consisted of 1 million pixels
# and Alex sold each pixel for $1 to advertisers.  The result was one of the most clever websites ever devised.
# 15 years later, the web page still generates about 70,000 visitors per month.

# This purpose of this project is to analyze the million dollar homepage to gain any interesting insights.


import requests, bs4, concurrent.futures, pprint, time

def checkLink(one_link, linkNum):
    global linkDict
    try:
        followLink = requests.get(one_link.get('href'), timeout=15)
        print(str(linkNum+1) + ',' + str(followLink.status_code) + ',' + one_link.get('title') + ','+ one_link.get('coords') + ',' + one_link.get('href') )
        linkDict[linkNum+1] = {'status': followLink.status_code, 'title': one_link.get('title'),'coords':one_link.get('coords'), 'href': one_link.get('href') }
    except:
        print(str(linkNum+1) + ',' + '0' + ',' + one_link.get('title') + ',' + one_link.get('coords') + ',' + one_link.get('href'))
        linkDict[linkNum+1] = {'status': 0, 'title': one_link.get('title'),'coords':one_link.get('coords'), 'href': one_link.get('href')}

res = requests.get('http://milliondollarhomepage.com/')
res.raise_for_status()

#Get all the HTML from the Million Dollar Homepage
soup = bs4.BeautifulSoup(res.text, features="lxml")

#get all the HTML elements within the area tag
links = soup.select('area')
#links = links[:30]
linkCount = len(links)

#set up final dictionary
linkDict = {}
for i in range(linkCount):
    linkDict[i+1]=''

#check each link for a request return code
processing_start = time.time()
pool = concurrent.futures.ThreadPoolExecutor(max_workers=100)
for i in range(linkCount):
    pool.submit(checkLink, links[i], i)

#Wait until all threads are finished then output the dictionary as it's own python file
pool.shutdown(wait=True)

print('Time taken (s): '+ str(round(time.time()-processing_start,2)))
resultFile = open('milliondollardata.py', 'w', encoding='utf-8')
resultFile.write('millionDollarData = ' + pprint.pformat(linkDict))
resultFile.close()

