# Lesson 7: Dictionaries and Sets

# !             Mutable | Ordered | Indexing | Duplicate Data
# ? LIST           ✔        ✔        ✔             ✔
# ? TUPLE          ❌       ✔        ✔             ✔
# ? SET            ✔        ❌       ❌            ❌
# ? DICTIONARY     ✔        ✔        ✔             ❌

# * Dictionary
band1 = {
    "vocals": "Plant",
    "guitar": "Page",
}

band2 = dict(vocals="Bon Jovi", guitar="Sambora")

print("Band 1: ", band1)
print("Band 2: ", band2)

# Access Items inside the dictionary
print("Vocals: ", band1["vocals"])
print("Guitar: ", band1.get("guitar"))

# List all keys and/or values
print("Band 1 Keys: ", band1.keys())
print("Band 1 Values: ", band1.values())

# List of key/value pairs as tuples
print("Band 1 Items (as Tuples): ", band1.items())

# Verify if a key exists
print("guitar" in band1)
print("drums" in band1)

# Update values in a dictionary
band1["vocals"] = "Coverdale"
band1.update({"bass": "JPJ"})
print("Updated Band 1: ", band1)

# Remove Items
print(
    "Popped Value: ", band1.pop("bass")
)  # Remove a specific key-value pair from the dictionary
print("Band 1: ", band1)

band1["drums"] = "Bonham"
print("Band 1 (With new Item): ", band1)

print(
    "Removed Item (Last Added): ", band1.popitem()
)  # Remove the last added item --- This returns the item as a tuple
print(band1)

# Delete and clear
band1["drums"] = "Bonham"
print("Band 1 (With new Item): ", band1)

del band1["drums"]  # Delete a key-value pair inside the dictionary
print("Band 1 (Deleted an Item): ", band1)

band2.clear()  # Clear out the items inside the dictionary
print("Band 2 (Cleared all Item): ", band2)

del band2  # Delete the dictionary

# ? Copy a Dictionary
# ! Bad Way to copy a dictionary
band2 = band1  # This only references band1, if changes are made to band2, band1 also changes.

# * Right Way to copy a dictionary
band2 = band1.copy()

print("Band 2 (Copy): ", band2)

band3 = dict(band1)  # Copy using the built-in function

# Loop through a dictionary
for x in band1:  # Return the keys
    print("Looped Keys: ", x)

for x in band1:  # Return the values
    print("Looped Values: ", band1[x])

for x in band1.keys():  # Looped Keys using keys() method
    print("Looped Keys (using .keys()): ", x)

for x in band1.values():  # Looped Values using values() method
    print("Looped Values (using .values()): ", x)

for x, y in band1.items():  # Looped Key-Value using items() method
    print("Looped Keys and Values (using .items()): ", x, y)

# ? Nested Dictionaries

# * The sane human way
myfamily = {
    "Emil": {"name": "Emil", "year": 2004},
    "Tobias": {"name": "Tobias", "year": 2007},
    "Linus": {"name": "Linus", "year": 2011},
}

print("My Family: ", myfamily)

# * Creating 3 dictionaries then adding them into a new dictionary
bruce = {"name": "Bruce", "year": 2000}
barry = {"name": "Barry", "year": 2007}
clark = {"name": "Clark", "year": 2011}

myOtherFamily = {"bruce": bruce, "barry": barry, "clark": clark}

print("My Other Family: ", myOtherFamily)

# Accessing nested dictionaries
print("The Dictionary: ", myfamily["Emil"])  # The dictionary
print(
    "Item inside the Dictionary: ", myfamily["Emil"]["name"]
)  # The item inside the dictionary


# * Sets
# ! NOTE: True and 1 are considered the same value, and also False and 0.
fruits = {"apple", "banana", "cherry", "apple"}

print("Set of Fruits", fruits)

set1 = {"apple", "banana", "cherry", "cherry"}  # Ignore repeated values
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print("Set 1 (Ignored duplicated Item): ", set1)
print("Set 2: ", set2)
print("Set 3: ", set3)

# Constructor Function
games = set(("League of Legends", "Teamfight Tactics", "VALORANT", "WildRift"))
print("Set of Games", games)
# Output {'VALORANT', 'WildRift', 'Teamfight Tactics', 'League of Legends'}
# ! NOTE: It was unordered``

# Access Items in a SET
# ! Can't access items by index or a key ONLY through LOOP or ask if a specific item is in the set

# Check if item exists in the set
print("DOTA 2" in games)

# Add Items in a set
games.add("Counter Strike 2")  # using .add() method

print("Newly Added Game in a SET", games)

newgames = set(("Apex Legends", "Dying Light", "Dead by Daylight"))

games.update(newgames)  # using .update() method

# Items inside a set doesn't have to be a set, it can be any iterable object (tuples, lists, dictionaries,etc)
games.update(["Mortal Kombat 11", ("Spiderman 2", "Alan Wake")])

print("Added New Games", games)

# Loop through items in a set
for x in games:
    print("Game", x)

# Join Sets
otherGames = set(("Game 1", "Game 2", "Game 3", "Game 4"))

myGames = games.union(otherGames)
print("My Games", myGames)

# Remove an item in a set
games.remove("Apex Legends")  # using .remove()
# ? NOTE: If item doesn't exist, RAISE an error!

games.discard("WildRift")  # using .discard()
# ? NOTE: If item doesn't exist, WILL NOT RAISE an error!

poppedgame = games.pop()  # using .pop()
# ? NOTE: This method will remove a random item

print("Games", games)
print("Popped Item", poppedgame)

# Clear a set
games.clear()

print("Cleared Set: ", games)

# del games # Delete the set
