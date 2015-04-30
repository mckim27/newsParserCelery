# -*- coding: utf-8 -*-

import sys
from modules.Parser import UrlParser
from ParseWorker import parse

parseUrlLinks = ['http://media.daum.net/economic/',
                 'http://media.daum.net/society/',
                 'http://media.daum.net/politics/',
                 'http://media.daum.net/foreign/',
                 'http://media.daum.net/culture/',
                 'http://media.daum.net/digital/']

def main() :
  global parseUrlLinks
  i = 0;
  urlCounts = len(parseUrlLinks)
  urlParser = UrlParser()
  while i < urlCounts:
    print "%d in %d : parsing `%s`" % (i,urlCounts, parseUrlLinks[i])
    addUrlLinks = urlParser.extractUrlLinks(parseUrlLinks[i])
    if not addUrlLinks == '' :  
      for newUrl in addUrlLinks :
        if(not newUrl in parseUrlLinks) : 
          #print newUrl 
          parseUrlLinks.append(newUrl)

    #parse.delay(parseUrlLinks[i], i)
    parse.apply_async((parseUrlLinks[i], i), queue='url', countdown=1, expires=20)

    urlCounts = len(parseUrlLinks)

    i = i + 1
    if i == 15 : break

if __name__ == "__main__":
  main()

