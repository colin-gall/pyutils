#!/usr/bin/env python
# -*- coding: utf-8 -*-

def web_scrape_crawl(url, crawl=None):
	"""web scraper returning bs4 object"""
	if crawl is not None:
		time.sleep(crawl)
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
