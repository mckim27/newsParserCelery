# -*- coding: utf-8 -*-

import time
from modules.Parser import dNewsParser
from modules.FileManager import *
from celeryconfig import app

print ' [*] Waiting for messages. To exit press CTRL+C'
@app.task
def parse(url, num):
    print " [x] Received %r : num %d " % (url, num)
    extractText = dNewsParser(url).titleParse().reduceToWords().getResult()
    FileManager.saveParseFile(extractText)
    #time.sleep(50)
    print " [x] Done"
