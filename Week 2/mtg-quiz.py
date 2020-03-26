#####################################
#                                   #
#  MTG Quiz                         #
#  by Eric Frierson                 #
#     and Fin Frierson              #
#####################################

# API Documentation at: https://scryfall.com/docs/api/cards/random

# libraries
import requests
import json

# functions
def pretty_print_card(card):
    if 'mana_cost' in card:
        mana_cost = str(card["mana_cost"])
    else:
        mana_cost = ""
    if 'flavor_text' in card:
        flavor_text = str(card["flavor_text"])
    else:
        flavor_text = ""
    print(card["name"] + " " + mana_cost)
    print(card["type_line"])
    print(card["oracle_text"])
    print("")
    print(flavor_text)
    print("")
    print(str(card['prices']['usd']))
    ### print out the flavor text if there is flavor text

# main code
mtg_api = "https://api.scryfall.com"
method = "/cards/random"

print('Loading...')

raw_response = requests.get(url = mtg_api+method)
card = raw_response.json()

# quiz: What is the CMC?
print("")
print(card["name"])
print("")
answer = int(input("What in the CMC of this card? "))
print("")
if (answer == card["cmc"]):
    print("Correct!")
else:
    print("Wrong!  The correct answer is "+str(int(card["cmc"]))+".")
print("")
Set_Name = input("What is the cards set?(full name)")
print("")
if (Set_Name.lower() == card["set_name"].lower()):
    print("Amazing! You are correct!")
else:
    print("Nope. The correct answer is "+str(card["set_name"])+".")
# quiz: What is the set name? (either the set abbreviation or full name is okay)

### ask the user what the set name is.
### check the answer against what is in the "card" variable
### if correct, print "correct" like above
### if incorrect, print "Wrong" and the name of the set, like above

# print out card details
pretty_print_card(card)
