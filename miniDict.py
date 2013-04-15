#!/usr/bin/python
#coding=utf-8

import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


"""
-------------------------------80size-------------------------------------------
"""

def cmdPr(explain):
	trans=""
	print("音标: [ %s ]" % explain['basic']['phonetic'])
	for i in explain['basic']['explains']:
		print(i)

def key():
	key = '258070906'
	keyfrom = 'commandtranslation'
	keyArray = [ key , keyfrom ]
	return keyArray

def getExplain(keyArray):
	word=sys.argv[1]
        url='http://fanyi.youdao.com/openapi.do?keyfrom=' + keyArray[1] + \
        	'&key=' + keyArray[0] + '&type=data&doctype=json&version' \
        	+ '=1.1&q=' + word
        transJson = requests.get(url).text
	explain = json.loads(transJson)
	return explain
	

if __name__ == "__main__":
	keyArray = key()
	explain = getExplain(keyArray)
	cmdPr(explain)



