
import urllib2
import json
import subprocess
import os
from sys import platform as _platform


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

	def downloadImage(self, imageUrl):
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
			imageFile = open('wallpaper.png', 'w')
			imageFile.write(image)


downloader = Downloader()

print "Starting to download Bing wallpaper."
imageUrl = downloader.getImageUrl()
downloader.downloadImage(imageUrl)

if _platform == "darwin":
	replPath = (os.getcwd() + "/wallpaper.png").replace('/', ':')[1:]
	commandToChange = "set the desktop picture to {\"%s\"} as alias" % (replPath)
	print "CommandToChange: " + commandToChange
	subprocess.call(["osascript", "-e", "tell app \"Finder\"", "-e", commandToChange, "-e", "end tell"])
	print "Wallpaper is set."
elif _platform == "win32":
	print "Windows implementation"
	print "Wallpaper is set."
#TODO make implementation for Windows
elif _platform == "linux" or _platform == "linux2":
	print "Linux implementation"
	print "Wallpaper is set."
	#TODO make implementation for Linux