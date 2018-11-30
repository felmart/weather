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

# create location string
def location_str(location):
    '''Join the location string to remove the space in the name'''
    location = ' '.join(location[1:])
    return location


# function to read key data from file
def reader(filename):
    '''
    Read the key data from a text file rather than rely on user input
    Store the key as a variable
    '''
    pass


# download the json data from openweather
# replace 'yourapikeyshouldbeinsertedhere' with your OWM API key
def url_builder(location, api):
    '''Build the full url'''
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=yourapikeyshouldbeinsertedhere' % (location)
    full_url = url + location + key
    return full_url


def fetcher(full_url):
    '''Fetch the weather forecast'''
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print('Access denied')


# load json data into a variable
def data_loader():
    '''Load the json data to a variable and print it out'''
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

def get_weather_data(location):
    '''Fetch weather data for a location'''
    pass


def more_locations(location):
    '''Fetch weather data for every location in the locations list'''
    pass


def get_locations(num):
    '''Get user input on list of locations.
    Let the user specify how many locations'''
    while num > 0:
        fetcher()
        num -= 1

def __main__():
    '''Main function'''
    pass


if name = __main__:
    main()
