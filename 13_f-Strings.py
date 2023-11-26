# Lesson 13: f-Strings

person = "Mark"
coins = 29

message = "" + person + " has " + str(coins) + " coins left."

# The Old Way using %s
message = "%s has %s coins left." % (person, coins)

# Using {} and .format()
message = "{} has {} coins left.".format(person, coins)

# By index, it follows the index of variables passed inside the .format() method
message = "{1} has {0} coins left.".format(coins, person)

# By their name
message = "{person} has {coins} coins left.".format(coins=coins, person=person)

# Using a dictionary
player = dict(person="Mark", coins=8)
# Keys here must be the same below inside the curly braces {}

message = "{person} has {coins} coins left.".format(**player)

# Using f-String function
message = f"{person} has {coins} coins left."

print(message)
