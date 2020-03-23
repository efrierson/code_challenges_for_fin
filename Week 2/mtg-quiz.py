#####################################
#                                   #
#  MTG Quiz                         #
#  by Eric Frierson                 #
#                                   #
#####################################

# libraries
import requests
import json

# functions
def pretty_print_card(card):
    if 'mana_cost' in card:
        mana_cost = str(card["mana_cost"])
    else:
        mana_cost = ""
    print(card["name"] + " " + mana_cost)
    print(card["type_line"])
    print(card["oracle_text"])
    print("")
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

# quiz: What is the set name? (either the set abbreviation or full name is okay)

### ask the user what the set name is.
### check the answer against what is in the "card" variable
### if correct, print "correct" like above
### if incorrect, print "Wrong" and the name of the set, like above

# print out card details
pretty_print_card(card)