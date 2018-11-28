#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import json


# input location using CL args
if len(sys.argv) < 2:
    print('Usage: weather.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])

# download the json data from openweather

# replace 'yourapikeyshouldbeinsertedhere' with your OWM API key
url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=yourapikeyshouldbeinsertedhere' % (location)


try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print('Access denied')

# load json data into a variable
weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
