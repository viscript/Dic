#!/usr/bin/python
#coding=utf-8

import requests
import json
import urllib2
import urllib
#import simplejson as json
import sys



if __name__ == "__main__":
	key='258070906'
	keyfrom='commandtranslation'
	word='translations'
	url='http://fanyi.youdao.com/openapi.do?keyfrom=' +keyfrom +'&key=' + key + '&type=data&doctype=json&version=1.1&q=' + word
	print(url)
	transJson = requests.get(url)
	print(transJson.text)
#	request=urllib2.urlopen(url)
#	data=request.read()
#	print(data)
