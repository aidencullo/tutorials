### TOPIC: Booleans III - or

# We have another operator of booleans called `or`

# `or` evaluates to True if at least one of the values passed is True

print(True or False)
print(True or False)
print(False or True)
print(False or False)

# Notice the last print statement was False because not even one value
# passed was True!

# Let's play another mystery game
from boolean_data import hasSilver
from boolean_data import hasBronze
from boolean_data import hasGold
from boolean_data import hasPlatinum

# We have a bag of minerals, what elements do they contain?

print(hasSilver or True)
print(hasSilver or False)
print(hasBronze and False)
print(hasBronze or hasBronze)
print(hasGold and hasSilver)
print(hasPlatinum or hasGold)
