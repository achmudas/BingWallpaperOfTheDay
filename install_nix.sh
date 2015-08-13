#!/bin/bash

PYTHON_PATH=$(whereis python)
# TODO install for the first time
#TODO check that probably it returns not empty answer: for MAC it returns nothing



if [[ $PYTHON_PATH ]]; then
	DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
	(crontab -l ; echo "0 * * * * $PYTHON_PATH $DIR/Downloader.py >> /tmp/bing.log 2>&1") | crontab
	echo "=========INSTALLATION COMPLETED!=========="
else
	echo 'PLEASE INSTALL PYTHON'
fi