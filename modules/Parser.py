# -*- coding: utf-8 -*-
import urllib, BeautifulSoup, re, string, urlparse
from konlpy.tag import Hannanum

class UrlParser :
  def __init__(self) :
    pass
  
  # 해당 url 페이지에서 링크를 추출함.
  def extractUrlLinks(self, url) :
    html = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(html)
    urlLinks = []
    for tag in soup.findAll('a', href=True):
      tag['href'] = urlparse.urljoin(url, tag['href'])
      # daum 뉴스 사이트 주소 형식에 rest 형식 url을 파싱함.
      if re.search('\/v\/', tag['href']) != None :
        #print 'find !!'
        filterPos = tag['href'].find('#')
        if filterPos != -1 :
          tag['href'] = tag['href'][:filterPos]

        urlLinks.append(tag['href'])
      #for end

    return list(set(urlLinks))

class dNewsParser :
  soup = ''
  result = ''
  def __init__(self, url) :
    html = urllib.urlopen(url)
    self.soup = BeautifulSoup.BeautifulSoup(html)
  
  # 해당 뉴스 페이지의 타이틀을 파싱. 
  def titleParse(self) :
    titles = ''
    try :
      for title in self.soup.find(id = 'newsTitleShadow' ).findAll(text=True, recursive=False):
        if re.search(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)", title) : continue
        titles = titles + title
    except :
      return self
    
    #print titles 
    self.result = titles
    return self

  # 해당 뉴스 페이지의 내용을 파싱
  def contentParse(self) :
    contents = ''
    try :
      for body in self.soup.find(id = 'newsBodyShadow' ).findAll(text=True, recursive=False):
        if re.search(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)", body) : continue
        contens = contents + body
    except :
      return self
    
    #print contents
    self.result = contents
    return self

  def getResult(self) :
    return self.result
   
  def reduceToWords(self) :
    hannanum = Hannanum()
    words = ''
    #for word in hannanum.nouns(unicode(texts, 'UTF-8')):
    if(self.result != '') :
      for word in hannanum.nouns(self.result):
        word = re.sub("[(*&]", "", word)
        if(len(word) > 1): words = word + '\n' + words
      #for end
      self.result =  words
      print words
    # if end
    return self
