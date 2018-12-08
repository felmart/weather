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

# read api key from file
api_key = ''
with open('key.txt', 'r') as key:
    api_key = key.read()

# download the json data from openweather
def url_builder(api):
    '''Build the full url'''
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=' % (location)
    full_url = url + api_key
    return full_url


def main():
    '''Main function'''
    try:
        response = requests.get(url_builder(api_key))
        response.raise_for_status
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

main()
