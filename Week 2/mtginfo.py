# required libraries
import requests
import json

# function to print out a card nicely for the user
# needs to be given a single card object from magicthegathering.io
def pretty_print_card(card):
    print(card["name"])
    if card["manaCost"]:
        print(card["manaCost"])
    print(card["type"])
    print(int(card["cmc"]))
# BEGIN

# We're going to use the APIs from magicthegathering.io
# Specifically, we're using the "/cards" method
# Documentation at https://docs.magicthegathering.io/#api_v1cards_list
mtg_api = "https://api.magicthegathering.io/v1"
method = "/cards"

# ask the user what card they want information about
name_to_search_for = input("What card do you want to know about? ")
print('Please wait.')
# prepare the request to the API by putting the user's input into the right parameter
# there's a lot of parameters we can use, documented at https://docs.magicthegathering.io/#api_v1cards_list
# here, we're just using the "name" to search by name of the card
parameters = {"name":name_to_search_for}

# build the API call - what URL the API is at and what parameters to send
# store what we get back in "raw_response"
raw_response = requests.get(url = mtg_api+method, params = parameters)

# a big long string is really hard to work with, so we convert it to JSON
response = raw_response.json()

if len(response["cards"])== 0:
    print("That's not a card!")
    quit()
# based on documentation from https://docs.magicthegathering.io/#api_v1cards_list...
# the cards are in a "cards" element, and I just want the first one, so I use index 0 to get it
#first_card = response["cards"][0]
for card in response["cards"]:
    # finally, give my function the first card to print
    pretty_print_card(card)
