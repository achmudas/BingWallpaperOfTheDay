BingWallpaperOfTheDay
=====================

Python script used to download Bing image of the day and set as Desktop background for Mac OS.

To install it, please execute
```
./install.sh
```
Make sure, that file is executable for current user. If not, please use `chmod`.

`install.sh` will create crontab entry, which will check for new Bing wallpaper of the day once per hour.

Current desktop image can be found in working directory: 
* if it's triggered by crontab - /Users/`current_user`/bing
* if manualy - ./bing

To download and change desktop background manually, please execute following commands:
```
python ./Downloader.py
```

If something goes wrong, please check logs in `/tmp/bing.log`
