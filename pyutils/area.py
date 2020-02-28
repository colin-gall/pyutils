#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from uszipcode import SearchEngine
from uszipcode import Zipcode

def get_city(zipcode):
	"""Get name of city for given zipcode."""
	try:
		engine = SearchEngine(simple_zipcode=True)
		location = engine.by_zipcode(zipcode)
		city = location.city
		return city
	except:
		return None

def get_state(zipcode):
	"""Get abbreviation of state for given zipcode."""
	try:
		engine = SearchEngine(simple_zipcode=True)
		location = engine.by_zipcode(zipcode)
		state = location.state
		return state
	except:
		return None

def get_zipcode(city):
	"""Get zipcode for a given city name."""
	try:
		engine = SearchEngine(simple_zipcode=True)
		location = engine.by_city(city, sort_by=Zipcode.population)
		zipcode = location[0].zipcode
		return zipcode
	except:
		return None
