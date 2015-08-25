#!/bin/bash

PYTHON_PATH=$(whereis python)

if [[ $PYTHON_PATH ]]; then
	DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
	$($PYTHON_PATH $DIR/Downloader.py >> /tmp/bing.log 2>&1)
	(crontab -l ; echo "0 * * * * $PYTHON_PATH $DIR/Downloader.py >> /tmp/bing.log 2>&1") | crontab
	echo "=========INSTALLATION COMPLETED!=========="
else
	echo 'PLEASE INSTALL PYTHON'
fi