#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
import requests.exceptions
from bs4 import BeautifulSoup as bs

def scrape_url(url, crawl=None):
	"""Web scraper that returns a BeautifulSoup object."""
	if crawl is not None:
		time.sleep(int(crawl))
	try:
		page = requests.get(url)
		if page.status_code == 200:
			contents = bs(page.text, 'lxml')
			return contents
		else:
			print("Error (status code {}).".format(page.status_code))
			return None
	except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as err:
		print(err)
		print("No internet connection. Is your Wi-Fi working?")
		return None
	except requests.HTTPError as err:
		print(err)
		print("Did you enter the correct year for the season you want stats from?")
		return None
	except ValueError as err:
		print(err)
		print("Did you accidentally enter a string instead of an integer for season year?")
		return None
	except Exception as err:
		print(err)
		print("Unknown error occurred while trying to establish connection.")
		return None

def check_connection():
	"""Checks for valid internet connection."""
	test_url = 'https://google.com'
	page = requests.get(test_url)
	if page.status_code != 200:
		return False
	return True
