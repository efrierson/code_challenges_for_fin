#############################
#    Quick Trade Service    #
#   For Checking prices to  #
#    Trade with friends     #
#      By Fin Frierson      #
#############################

import requests
import json

mtg_api = "https://api.scryfall.com"
method = "/cards/search"

card_name = input("What card would you like to find the value of? ")
parameters = {"q":card_name}
raw_response = requests.get(url = mtg_api+method,params = parameters)
all_cards = raw_response.json()
print(str(all_cards))
print("")
#print(str(int(card["prices"]["usd"])))
for card in all_cards['data']:
    print(str(card))
    print(str(card['name']))
    print(str(card['prices']['usd']))
    print(str(card['prices']['usd_foil']))
    
