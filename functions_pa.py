#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:30:58 2026

@author: johannramos
"""

import requests
country = requests.get('https://countries.dev/alpha/US').json()
# print(country['name'], country['capital'])
print(country)
region = requests.get('https://countries.dev/region').json()
print(region)