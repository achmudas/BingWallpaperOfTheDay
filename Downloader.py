
import urllib2
import json
import subprocess
import os
from sys import platform as _platform
from datetime import datetime
import shutil


class Downloader:

	def getImageUrl(self):
		try:
			response = urllib2.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
		except urllib2.URLError as e:
			if hasattr(e, 'reason'):
				print 'Cannot reach the server.'
				print 'Reason: ', e.reason
			elif hasattr(e, 'code'):
				print 'The server couldn\'t get image url.'
				print 'Error code: ', e.code
		else:
			jsonResponse = response.read()
			jsonDoc = json.loads(jsonResponse)
			return jsonDoc["images"][0]['url']

	def downloadImage(self, imageUrl, fileName):
		try:
			response = urllib2.urlopen("http://www.bing.com" + imageUrl)
		except urllib2.URLError as e:
			if hasattr(e, 'reason'):
				print 'Cannot reach the server.'
				print 'Reason: ', e.reason
			elif hasattr(e, 'code'):
				print 'The server couldn\'t fulfill the request.'
				print 'Error code: ', e.code
		else:
			image = response.read()
			imageFile = open(fileName, 'w+b')
			imageFile.write(image)



if os.path.exists(os.getcwd() + '/bing'):
	shutil.rmtree(os.getcwd() + '/bing')

os.mkdir('bing')

downloader = Downloader()

print "Starting to download Bing wallpaper."
imageUrl = downloader.getImageUrl()
fileName = 'bing/wallpaper_' + datetime.now().strftime("%Y_%M_%d_%H_%M") + '.png'
downloader.downloadImage(imageUrl, fileName)

if _platform == "darwin":
	replPath = (os.getcwd() + '/' + fileName).replace('/', ':')[1:]
	commandToChange = "set the desktop picture to {\"%s\"} as alias" % (replPath)
	subprocess.call(["osascript", "-e", "tell app \"Finder\"", "-e", commandToChange, "-e", "end tell"])
	print "Wallpaper is set."