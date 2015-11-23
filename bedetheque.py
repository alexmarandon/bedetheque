import re
from bedetheque_lib import *


url = "http://www.bedetheque.com"
re_strg_page = "http://www.bedetheque.com/bandes_dessinees.+"
re_strg_serie = "http://www.bedetheque.com/serie.+"
fname_page = "bdt_pages.txt"
fname_series = "bdt_series.txt"

#parse home page to extract series pages links
pages = parse_child_links_file(url, re_strg_page, fname_page)

#dump all series in series file
series = list()
for page in pages:
    fnamepage = re.findall("([^/]+)\.[a-z]+$",page)[0]
    fnamepage = "bdt_" + fnamepage + ".txt"
    series = series + parse_child_links_file(page, re_strg_serie, fnamepage)


fhand = open(fname_series,"w")
print "Writing Series", fname_series
for serie in series: 
    try : fhand.write(serie+"\n")
    except : continue
fhand.close()





