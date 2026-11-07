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
    wanted_country = requests.get(f'https://countries.dev/name/{wanted_country.lower()}').json()
    country = wanted_country[0]['name']
    currencies_list = [currency['name'] for currency in wanted_country[0]['currencies']]
    if len(currencies_list) == 1:
        currencies = currencies_list[0]
    elif len(currencies_list) == 2:
        currencies = ' and '.join(currencies_list)
    else:
        currencies = ', '.join(currencies_list[:-1]) + ' and ' + currencies_list[-1]
    languages_list = [language['name'] for language in wanted_country[0]['languages']]
    if len(languages_list) == 1:
        languages = languages_list[0]
    elif len(languages_list) == 2:
        languages = ' and '.join(languages_list)
    else:
        languages = ', '.join(languages_list[:-1]) + ' and ' + languages_list[-1]
    print(f"""{country}'s capital is {wanted_country[0]['capital']}
{country}'s currency or currencies include {currencies}
{country}'s language or languages include {languages}""")
else:
    print(f"That country is not in {which_region}") #do it with try/except
    
#make sure to make them into functions and have different files
