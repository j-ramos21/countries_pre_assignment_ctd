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
#@return wanted_region The fetched API of user's chosen region
def what_region():
    #getting all the regions from the API
    all_regions = requests.get("https://countries.dev/regions").json()
    #while loop that restarts when there is an incorrect input (region) and moves on when the input is an existing region
    while True:
        #prompts the user what region the country they want to know about is in
        which_region = input("What region is your country in? (case-sensitive) ")
        #conditional statement that if the chosen region is in the regions list then it fetches the region from the API or else the list of all the regions is printed and the user is prompted again
        if which_region in all_regions:
            #gets the wanted region from the API
            wanted_region = requests.get(f"https://countries.dev/region/{which_region}").json()
            return which_region, wanted_region
        else:
            #lets the user know there has been an error, prints all the regions, and while loop starts again
            print(f"""Error: Blank input, region does not exist, or not capitalized.
These are all the regions: {', '.join(all_regions[:-1])}, and {all_regions[-1]}
Please choose one.""")

#This function prompts the user what country they want to know about. It uses the list of countries from which_region to make sure the country the user picks is in the chosen region. It asks you again if there was an incorrect input. After a correct input, it prints the capital, currencies, and languages of the chosen country.
#@param which_region The region the user chose from what_region
#@param wanted_region The fetched API of user's chosen region from what_region
#@return country The name of the user's chosen country
#@return capital The capital of the user's chosen country
#@return currencies All the currencies of the user's chosen country
#@return languages All the languages of the user's chosen country
def what_country(which_region, wanted_region):
    #prompts the user what country they want to know about
    names_of_countries = [country['name'] for country in wanted_region]
    #prints all the countries that are in the chosen region
    print(f"These are the countries in the region: {', '.join(names_of_countries[:-1])}, and {names_of_countries[-1]}")
    #while loop that restarts when there is an incorrect input (country) and moves on when the input is an existing region
    while True:
        #prompts the user what country they want to know about
        which_country = input("What country do you want to know about? (case-sensative) ")
        #conditional statement that if the chosen country is in the list of all the countries in the region then it fetches the country and the fields from the API or else the user is again prompted to enter a country from the list of countries
        if which_country in names_of_countries:
            #gets the chosen country from the API
            wanted_country = requests.get(f'https://countries.dev/name/{which_country.lower()}').json()
            #saved the name of the country
            country = wanted_country[0]['name'] 
            #saved the capital of the country
            capital = wanted_country[0]['capital']     
            #got the currencies' names from the wanted country
            currencies_list = [currency['name'] for currency in wanted_country[0]['currencies']]
            #conditional statement that decides how the currencies are displayed. If there is only one, then just print the one currency. If there are more than one, then there will be commas and an "and".
            if len(currencies_list) == 1:
                currencies = currencies_list[0]
            elif len(currencies_list) == 2:
                currencies = ' and '.join(currencies_list)
            else:
                currencies = ', '.join(currencies_list[:-1]) + ' and ' + currencies_list[-1]
                
            #conditional statement that decides how the languages are displayed. If there is only one, then just print the one language. If there are more than one, then there will be commas and an "and".
            languages_list = [language['name'] for language in wanted_country[0]['languages']]
            if len(languages_list) == 1:
                languages = languages_list[0]
            elif len(languages_list) == 2:
                languages = ' and '.join(languages_list)
            else:
                languages = ', '.join(languages_list[:-1]) + ', and ' + languages_list[-1]
            return country, capital, currencies, languages
        else:
            #lets the user know there has been an error with the input and while loop starts again
            print(f"""Error: {which_country} is not in {which_region}, not capitalized, does not exist, or blank input.
Please choose one from the list above.""")

#This function displays three fields of the country, the capital, currencies, and languages
#@param country The name of the user's chosen country
#@param capital The capital of the user's chosen country
#@param currencies All the currencies of the user's chosen country
#@param languages All the languages of the user's chosen country
#@return none
def information(country, capital, currencies, languages):
    #prints the capital, currencies, and languages of the chosen country
    print(f"""{country}'s capital is {capital}
{country}'s currency or currencies include {currencies}
{country}'s language or languages include {languages}""")

#This function is the main function. Executes the fetching (what_region()), processing (what_country(which_region, wanted_region)), and the displaying (information(country, capital, currencies, languages))
#@param none
#@return none
def main():
    which_region, wanted_region = what_region()
    country, capital, currencies, languages = what_country(which_region, wanted_region)
    information(country, capital, currencies, languages)