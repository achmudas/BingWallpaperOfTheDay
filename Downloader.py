
import urllib2
import json
import subprocess
import os


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
imageUrl = downloader.getImageUrl()

downloader.downloadImage(imageUrl)


currentWorkingDirectory = os.getcwd()

pathToWallpaper = currentWorkingDirectory + "/wallpaper.png"

subprocess.call(["osascript", "-e", "tell app \"Finder\"", "-e", 
	"set the desktop picture to {\"Macintosh HD:Users:achmudas:Documents:Projects:BingWallpaperOfTheDay:wallpaper.png\"} as alias", "-e", "end tell"])


