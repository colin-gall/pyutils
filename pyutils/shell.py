#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import math
import datetime

class colors:
	reset='\033[0m'
	bold='\033[01m'
	underline='\033[04m'
	red='\033[91m'
	green='\033[92m'
	yellow='\033[93m'
	pink='\033[95m'
	cyan='\033[96m'
	grey='\033[90m'
	white='\033[97m'

def clear_screen():
	"""Clears terminal window screen."""
	if sys.platform == 'windows':
		os.system('cls')
	else:
		os.system('clear')

def flush_screen():
	"""Deletes previous output line in terminal."""
	sys.stdout.write('\x1b[1A')
	sys.stdout.write('\x1b[2K')

def progress_bar(x, y):
	"""Progress bar to display status updates in terminal."""
	progress = ''
	for j in range(int(x)):
		progress += '#'
	for k in range(int(y) - int(x)):
		progress += '-'
	percentage = math.ceil((x / y) * 100)
	bar = "[{} {}%]".format(progress, str(percentage))
	return bar

def current_time(military=True):
	now = datetime.datetime.now().strftime('%H:%M')
	hour = int(datetime.datetime.now().strftime('%H'))
	if military is False:
		if hour > 12:
			now = str(hour - 12) + datetime.datetime.now().strftime(':%M') + 'pm'
		else:
			now = now + 'am'
	return now
