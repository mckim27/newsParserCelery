# -*- coding: utf-8 -*-

import os, random, sys, types, string

class FileManager :
  def __init__(self):
    pass

  @staticmethod
  def getFileNames(path) :
    data = {}
    for dir_entry in os.listdir(path):
      dir_entry_path = os.path.join(path, dir_entry)
      if os.path.isfile(dir_entry_path):
        with open(dir_entry_path, 'r') as my_file:
          data[dir_entry] = my_file.read()

    return data
  
  # 랜덤 문자 생성기
  @staticmethod
  def randomStringGenerator():
    asciiUpper = string.ascii_uppercase
    asciiLower = string.ascii_lowercase
    digits = string.digits
    return ''.join(random.choice(asciiUpper + asciiLower + digits) for x in range(48))

  # 파라미터로 넘어온 문자들을 텍스트 파일로 저장. 파일이름은 랜덤 문자열 사용.
  @staticmethod
  def saveParseFile(content, fname = 'init'):
    # data 폴더 없으면 생성
    if not os.path.exists('./data'):
      os.makedirs('./data')
    if('init' == fname) : fname = FileManager.randomStringGenerator()

    if os.path.isfile('data/' + fname):
      print "duplicate !!"
      saveParseFile(content, 'init')
    else:
      f = open('data/' + fname, 'w')
      f.write(content.encode("UTF-8"))
      f.close()
