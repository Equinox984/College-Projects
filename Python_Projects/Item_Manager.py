"""Item Manager"""
# Creating the Inventory
inventory = ["sword", "healing potion",
             "shield", "armor", "letter for yennefer"]
print(inventory, "\n")

# The Character Obtains a Gold  Coin
inventory.insert(0, "gold coin")
print(inventory, "\n")

# The character gets wounded by a troll looking for his lost brother, in the woods
# The character uses healing potion
inventory.remove("healing potion")

# In the haste of using the healing potion the character drops the sword.
inventory.pop(1)
print(inventory, "\n")

# The character recovers the sword and strike the troll through the heart...
inventory.append("sword")

# The character decides to check if the letter for yennefer is still in the inventory.
print(inventory.index("letter for yennefer"))

# The character decides to check if there is some healing potion left in the inventory.
print(inventory.count("healing potion"))
