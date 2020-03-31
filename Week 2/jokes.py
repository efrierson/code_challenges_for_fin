import random

jokes = []
jokes.append("Why did the chicken cross the road?  To get to the other side.")
jokes.append("A horse walks into a bar.  The bartender asks, Why the long face?")
jokes.append("I asked my dad for a bookmark.  He started crying and said, You don't even know my name is Eric?")

random_joke = random.choice(jokes)
speech = random_joke

print(speech)