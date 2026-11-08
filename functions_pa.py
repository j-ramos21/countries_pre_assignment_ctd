#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:30:58 2026

@author: johannramos
"""
import requests
#This function prompts the user what region is their country. It shows all the regions if there was an error. After a correct input, it prints all the countries in the region
#@param none
#@return which_region The region the user chose
#@return names_of_countries The list of all the countries in the region
def what_region():
    #getting all the regions from the API
    all_regions = requests.get("https://countries.dev/regions").json()
    #while loop that restarts when an incorrect region is inputted it restarts and moves on when the input is a existing region
    while True:
        #prompts the user what region the country they want to know about is in
        which_region = input("What region is your country in? (case-sensitive) ")
        #conditional statement that if the chosen region is in the regions list then it prints all the countries in the region or else the list of all the regions is printed and the user is prompted again
        if which_region in all_regions:
            #gets the wanted region from the API
            wanted_region = requests.get(f"https://countries.dev/region/{which_region}").json()
            #gets the names of all the countries in the region
            names_of_countries = [country['name'] for country in wanted_region]
            #prints all the countries in the region
            print(f"These are the countries in the region: {', '.join(names_of_countries[:-1])}, and {names_of_countries[-1]}")
            #returns which_region, names_of_countries
            return which_region, names_of_countries
        else:
            #lets the user know there has been an error, prints all the regions, and prompts the user again
            print(f"""Error: Blank input or region does not exist.
These are all the regions: {', '.join(all_regions[:-1])}, and {all_regions[-1]}
Please choose one.""")

#This function prompts the user what country they want to know about. It uses the list of countries from which_region to make sure the country the user picks is in the chosen region. It asks you again if there was an incorrect input. After a correct input, it prints the capital, currencies, and languages of the chosen country.
#@param which_region The region the user chose from what_region
#@param names_of_countries The list of all the countries in the region from what_region
#@return none
def what_country(which_region, names_of_countries):
    #prompts the user what country they want to know about
    wanted_country = input("What country do you want to know about? ")
    #conditional statement that if the chosen country is in the list of all the countries in the region
    if wanted_country in names_of_countries:
        #gets the chosen country from the API
        wanted_country = requests.get(f'https://countries.dev/name/{wanted_country.lower()}').json()
        #saved the name of the country
        country = wanted_country[0]['name']
        
        #got the currencies' names from the wnated country
        currencies_list = [currency['name'] for currency in wanted_country[0]['currencies']]
        #conditional statement that decides how the currencies are displayed. If there is only one, then just print the one currency. If there are more than one, then there will be commas and a "and".
        if len(currencies_list) == 1:
            currencies = currencies_list[0]
        elif len(currencies_list) == 2:
            currencies = ' and '.join(currencies_list)
        else:
            currencies = ', '.join(currencies_list[:-1]) + ' and ' + currencies_list[-1]
            
        #conditional statement that decides how the languages are displayed. If there is only one, then just print the one language. If there are more than one, then there will be commas and a "and".
        languages_list = [language['name'] for language in wanted_country[0]['languages']]
        if len(languages_list) == 1:
            languages = languages_list[0]
        elif len(languages_list) == 2:
            languages = ' and '.join(languages_list)
        else:
            languages = ', '.join(languages_list[:-1]) + ', and ' + languages_list[-1]
         
        #prints the capital, currencies, and languages
        print(f"""{country}'s capital is {wanted_country[0]['capital']}
{country}'s currency or currencies include {currencies}
{country}'s language or languages include {languages}""")
    else:
        #prints there has been an error if the input was incorrect and prompts the user again
        print(f"""Error: Country is not in {which_region}, does not exist, or blank input.
Please choose one from the list above.""")
        what_country(which_region, names_of_countries)

def main():
    which_region, names_of_countries = what_region()
    what_country(which_region, names_of_countries)