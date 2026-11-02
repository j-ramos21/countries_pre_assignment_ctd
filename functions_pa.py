#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:30:58 2026

@author: johannramos
"""

import requests
which_region = input("What region is your country in? ")
wanted_region = requests.get(f"https://countries.dev/region/{which_region}").json()
names_of_countries = [country['name'] for country in wanted_region]
print(f"These are the countries in the region: {names_of_countries}")
wanted_country = input("What country do you want to know about? ")
if wanted_country in names_of_countries:
    wanted_country = requests.get(f'https://countries.dev/alpha/{wanted_country}').json()
    print(f"""{wanted_country}'s capital is {wanted_country['capital']}
          {wanted_country}'s currency or currencies include {wanted_country['currencies']}""")

# country = requests.get('https://countries.dev/alpha/US').json()
# print(country['name'], country['capital'])
# print(country['region'])
# region = requests.get('https://countries.dev/region').json()
# print(region) 
# url = "https://countries.dev/region/Asia"
# response = requests.get("https://countries.dev/region/Asia").json()
# print(response['name'])