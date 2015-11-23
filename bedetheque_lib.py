import urllib
import re
from bs4 import BeautifulSoup

def parse_child_links_file(url, re_strg, fname):
    
    childurls = list()
    #does the file exist?
    #yes - just open it and dump into childurls
    try:
        fhand = open(fname)
        print "Opening", fname
        for line in fhand:
            line = line.strip()
            childurls.append(line)
        fhand.close()
    #no - create it by parsing the url
    except:
        print "Parsing", url
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
    
        tags = soup('a')
        #loop through <a> tags
        for tag in tags:
            urlstring = tag.get("href", None)
            #match regexp passed in args
            try : urlre = re.findall(re_strg, urlstring)
            except : continue
            if len(urlre) != 1 : continue
            urlstring = urlre[0].strip()
            #append list with unique urls only
            if urlstring not in childurls: 
                print "URL found:", urlstring
                childurls.append(urlstring)
        print "Writing", fname
        #create file
        fhand = open(fname,"w")
        for page in childurls: 
            try : fhand.write(page+"\n")
            except : continue
        fhand.close()
    
    return childurls


def parse_child_links(url, re_strg):
    
    childurls = list()
    print "Parsing", url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    
    tags = soup('a')
    for tag in tags:
        urlstring = tag.get("href", None)
        #match regexp passed in args
        try : urlre = re.findall(re_strg, urlstring)
        except : continue
        if len(urlre) != 1 : continue
        urlstring = urlre[0].strip()
        #append list with unique urls only
        if urlstring not in childurls: 
            print "URL found:", urlstring
            childurls.append(urlstring)

    
    return childurls

def parse_all_links(url):
    
    childurls = list()
    print "Parsing", url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    
    tags = soup('a')
    for tag in tags:
        urlstring = tag.get("href", None)
        print "URL found:", urlstring
        childurls.append(urlstring)
    return childurls
    

