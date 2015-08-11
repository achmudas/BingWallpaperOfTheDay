#!/bin/bash

PYTHON_PATH=$(whereis python)

if [[ $PYTHON_PATH ]]; then
	DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
	(crontab -l ; echo "0 0,4,8,12,16,20 * * * python $DIR/Downloader.py") | crontab
else
	echo 'PLEASE INSTALL PYTHON'
fi