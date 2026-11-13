#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:30:58 2026

@author: johannramos
"""
import requests
#This function fetches all the region and the country the user wants. It prompts the user what region is their country in. It shows all the regions if there was an incorrect input. After a correct input
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

#This function prompts the user what country they want to know about. It uses the list of countries from which_region to make sure the country the user picks is in the chosen region. It asks you again if there was an incorrect input. After a correct input, it prints the capital, currencies, and languages of the chosen country. If there is only one country in the chosen region, then it will not prompt the user since there is only one option.
#@param which_region The region the user chose from what_region()
#@param wanted_region The fetched API of user's chosen region from what_region()
#@return country The name of the user's chosen country
#@return capital The capital of the user's chosen country
#@return currencies All the currencies of the user's chosen country
#@return languages All the languages of the user's chosen country
#@return currencies_list List of all the currencies of the user's chosen country
#@return languages_list List of all the languages of the user's chosen country
def what_country(which_region, wanted_region):
    #creates a list of all the countries in the region
    names_of_countries = [country['name'] for country in wanted_region]
    #conditional statement that if there is more than one country in the region then it prompts the user to choose a country or else it lets the user know the only country in the region and there's no prompt since there's only one country
    if len(names_of_countries) > 1:
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
                #conditional statement that if the country does have a capital then it saves it or else the capital is nonexistent
                if 'capital' in wanted_country[0]:
                    #saved the capital of the country
                    capital = wanted_country[0]['capital'] 
                else:
                    #no capital, so it is set to nonexistent
                    capital = "nonexistent"
    
                #conditional statement that if the country has at least one currency then it saves them or else the currency is nonexistent
                if 'currencies' in wanted_country[0]:
                    #got the currencies' names from the wanted country
                    currencies_list = [currency['name'] for currency in wanted_country[0]['currencies']]
                    #conditional statement that decides how the currencies are displayed. If there is only one, then just print the one currency. If there are more than one, then there will be commas and an "and".
                    if len(currencies_list) == 1:
                        #the only currency is printed
                        currencies = currencies_list[0]
                    elif len(currencies_list) == 2:
                        #the two currencies are printed with an "and"
                        currencies = ' and '.join(currencies_list)
                    else:
                        #the currencies are printed with commas and an "and"
                        currencies = ', '.join(currencies_list[:-1]) + ' and ' + currencies_list[-1]
                else:
                    #no currency, so it is set to nonexistent and the list is empty
                    currencies = "nonexistent"
                    currencies_list = []
                
                #conditional statement that if the country has at least one language then it saves them or else the language is nonexistent
                if 'languages' in wanted_country[0]:
                    #got the languages' names from the wanted country
                    languages_list = [language['name'] for language in wanted_country[0]['languages']]
                    #conditional statement that decides how the languages are displayed. If there is only one, then just print the one language. If there are more than one, then there will be commas and an "and".
                    if len(languages_list) == 1:
                        #the only language is printed
                        languages = languages_list[0]
                    elif len(languages_list) == 2:
                        #the two languages are printed with an "and"
                        languages = ' and '.join(languages_list)
                    else:
                        #the languages are printed with commas and an "and"
                        languages = ', '.join(languages_list[:-1]) + ', and ' + languages_list[-1]
                else:
                    #no language, so it is set to nonexistent and the list is empty
                    languages = "nonexistent"
                    languages_list = []
                return country, capital, currencies, languages, currencies_list, languages_list
            else:
                #lets the user know there has been an error with the input and while loop starts again
                print(f"""Error: {which_country} is not in {which_region}, not capitalized, does not exist, or blank input.
Please choose one from the list above.""")
    else:
        #lets the user know there is only one country in the chosen region
        print(f"This is the only country in the region: {names_of_countries[0]}")
        #gets the only country in the reigon from the API
        wanted_country = requests.get(f'https://countries.dev/name/{names_of_countries[0].lower()}').json()
        #saved the name of the country
        country = wanted_country[0]['name'] 
        #conditional statement that if the country does have a capital then it saves it or else the capital is nonexistent
        if 'capital' in wanted_country[0]:
            #saved the capital of the country
            capital = wanted_country[0]['capital'] 
        else:
            #no capital, so it is set to nonexistent
            capital = "nonexistent"
        #conditional statement that if the country has at least one currency then it saves them or else the currency is nonexistent
        if 'currencies' in wanted_country[0]:
            #got the currencies' names from the wanted country
            currencies_list = [currency['name'] for currency in wanted_country[0]['currencies']]
            #conditional statement that decides how the currencies are displayed. If there is only one, then just print the one currency. If there are more than one, then there will be commas and an "and".
            if len(currencies_list) == 1:
                #the only currency is printed
                currencies = currencies_list[0]
            elif len(currencies_list) == 2:
                #the two currencies are printed with an "and"
                currencies = ' and '.join(currencies_list)
            else:
                #the currencies are printed with commas and an "and"
                currencies = ', '.join(currencies_list[:-1]) + ' and ' + currencies_list[-1]
        else:
            #no currency, so it is set to nonexistent and the list is empty
            currencies = "nonexistent"
            currencies_list = []
        
        #conditional statement that if the country has at least one language then it saves them or else the language is nonexistent
        if 'languages' in wanted_country[0]:
            #got the languages' names from the wanted country
            languages_list = [language['name'] for language in wanted_country[0]['languages']]
            #conditional statement that decides how the languages are displayed. If there is only one, then just print the one language. If there are more than one, then there will be commas and an "and".
            if len(languages_list) == 1:
                #the only language is printed
                languages = languages_list[0]
            elif len(languages_list) == 2:
                #the two languages are printed with an "and"
                languages = ' and '.join(languages_list)
            else:
                #the languages are printed with commas and an "and"
                languages = ', '.join(languages_list[:-1]) + ', and ' + languages_list[-1]
        else:
            #no language, so it is set to nonexistent and the list is empty
            languages = "nonexistent"
            languages_list = []
        return country, capital, currencies, languages, currencies_list, languages_list
        

#This function displays three fields of the country, the capital, currencies, and languages. It also displays if the fields are nonexistent.
#@param country The name of the user's chosen country from what_country(which_region, wanted_region)
#@param capital The capital of the user's chosen country from what_country(which_region, wanted_region)
#@param currencies All the currencies of the user's chosen country from what_country(which_region, wanted_region)
#@param languages All the languages of the user's chosen country from what_country(which_region, wanted_region)
#@param currencies_list List of all the currencies of the user's chosen country from what_country(which_region, wanted_region)
#@param languages_list List of all the languages of the user's chosen country from what_country(which_region, wanted_region)
#@return none
def information(country, capital, currencies, languages, currencies_list, languages_list):
    #prints the capital of the chosen country or that it is nonexistent
    print(f"{country}'s capital is {capital}")
    
    #conditional statement that if the list of currencies has less than or equal to 1 item then it uses "is" or else it uses "are"
    if len(currencies_list) <= 1:
        #prints the only currency or that it is nonexistent
        print(f"{country}'s currency is {currencies}")
    else:
        #prints all the currencies
        print(f"{country}'s currencies are {currencies}")
    
    #conditional statement that if the list of languages has less than or equal to 1 item then it uses "is" or else it uses "are"
    if len(languages_list) <= 1:
        #prints the only language or that it is nonexistent
        print(f"{country}'s language is {languages}")
    else:
        #prints all the languages
        print(f"{country}'s languages are {languages}")

#This function is the main function. Executes the fetching (what_region()), processing (what_country(which_region, wanted_region)), and the displaying (information(country, capital, currencies, languages))
#@param none
#@return none
def main():
    which_region, wanted_region = what_region()
    country, capital, currencies, languages, currencies_list, languages_list = what_country(which_region, wanted_region)
    information(country, capital, currencies, languages, currencies_list, languages_list)