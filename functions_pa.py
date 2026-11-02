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
wanted_country = input("What country do you want to know about? ") #have at least one interaction of filter, lookup, or comparison
if wanted_country in names_of_countries:
    wanted_country = requests.get(f'https://countries.dev/name/{wanted_country.lower()}').json()
    print(f"""{wanted_country[0]['name']}'s capital is {wanted_country[0]['capital']}
{wanted_country[0]['name']}'s currency or currencies include {wanted_country[0]['currencies'][0]['name']}
{wanted_country[0]['name']}'s language or languages include {wanted_country[0]['languages'][0]['name']}""")
else:
    print(f"That country is not in {which_region}") #do it with try/except
    
#make sure to make them into functions and have different files
