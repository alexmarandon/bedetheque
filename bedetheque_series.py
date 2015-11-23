import urllib
import re
from bs4 import BeautifulSoup
from bedetheque_lib import *

fname_series = "bdt_series.txt"
fname_parsed_series = "bdt_parsed_series.txt"
re_strg_bd = "http://www.bedetheque.com/BD[^#]+"

series = list()
fhand = open(fname_series)
print "Opening", fname_series
i = 0
for line in fhand:
    line = line.strip()
    series.append(line)
    i = i + 1
fhand.close()
print i, "Imported Series"

num = raw_input('Enter - ')



url = series[int(num)]


print "Parsing", url
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
linktags = soup('a')
childurls = list()
for tag in linktags:
    #print 'TAG:',tag
    urlstring = tag.get("href", None)
    #print urlstring
    if urlstring: urlstring = urlstring.strip().encode("utf8")
    #match regexp passed in args
    try : urlre = re.findall(re_strg_bd, urlstring)
    except : continue
    if len(urlre) != 1 : continue
    urlstring = urlre[0].strip()
    #append list with unique urls only
    if urlstring not in childurls: 
        #print "URL found:", urlstring
        childurls.append(urlstring)


serie = dict()
listitem =soup.find("div",{"class":"single-content serie"}).ul.findAll("li")
serie['genre'] = listitem[0].span.contents[0].encode("utf8")
serie['parution'] = listitem[1].span.contents[0].encode("utf8")
serie['tomes'] = int(listitem[2].contents[1])
serie['id'] = int(listitem[3].contents[1])
serie['origine'] = listitem[4].contents[1].encode("utf8")
serie['langue'] = listitem[5].contents[2].encode("utf8")
serie['resume'] = soup.find("div",{"class":"single-content serie"}).p
serie['listeurlbd'] = childurls

print serie



#<div class=>


