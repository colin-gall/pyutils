#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import schedule
import time

def queue_job(job, start_time, start_day, military_time=True, time_of_day='AM'):
	"""Queues package or script to run in background."""
	try:
		start_time = time.strptime(start_time, '%H:%M')
	except ValueError as err:
		print(err)
		print("Start time {} is not a valid format.".format(start_time))
		return
	except Exception as err:
		print(err)
		print("Error occured while attempting to schedule job.")
		sys.exit()
	if military_time is False:
		if time_of_day == 'PM':
			hour = start_time.tm_hour
			minute = start_time.tm_min
			if hour <= 12:
				hour = hour + 12
				new_time = str(hour) + ':' + str(minute)
				start_time = time.strptime(new_time, '%H:%M')
	if len(str(start_time.tm_min)) == 1:
		start_time = str(start_time.tm_hour) + ':0' + str(start_time.tm_min)
	else:
		start_time = str(start_time.tm_hour) + ':' + str(start_time.tm_min)
	days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	days_of_week_short = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
	if start_day not in days_of_week and start_day not in days_of_week_short:
		print("Start day {} is not a valid format.".format(start_day))
		return
	elif start_day in days_of_week_short:
		day_index = days_of_week_short.index(start_day)
		start_day = days_of_week[day_index]
	if start_day == 'Monday':
		schedule.every().monday.at(start_time).do(job)
	elif start_day == 'Tuesday':
		schedule.every().tuesday.at(start_time).do(job)
	elif start_day == 'Wednesday':
		schedule.every().wednesday.at(start_time).do(job)
	elif start_day == 'Thursday':
		schedule.every().thursday.at(start_time).do(job)
	elif start_day == 'Friday':
		schedule.every().friday.at(start_time).do(job)
	elif start_day == 'Saturday':
		schedule.every().saturday.at(start_time).do(job)
	elif start_day == 'Sunday':
		schedule.every().sunday.at(start_time).do(job)

def run_job():
	"""Schedules and runs queued jobs."""
	while True:
		x = 0
		current_time = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min)
		print("The time is {}. Still running jobs in the background!".format(current_time))
		while x < 60:
			schedule.run_pending()
			time.sleep(60)
			x += 1
