"""Dictionary Toolkit - Topic: Dictionaries (Syntax and Methods)"""

# Step #1: Create a Dictionary of Phone Contacts
contacts = {
    "Alice": "555 - 1234",
    "Bob": "555 - 5678",
    "Carlos": "555 - 9012",
}


# Step #2: Access a Value using .get() method
name = str(input("Enter a Contact Name -> "))
phone = contacts.get(name)

if not phone:
    print("\nERROR: 404 NOT FOUND")
else:
    print(f"""
Contact Found!
Name: {name}
Phone: {phone}\n""")


# Step 3: Display all the Keys in the Dictionary
print("Contact Names:")
for name in contacts.keys():
    print(f"-{name}")

# Step 4: Display all Values in the Dictionary using the .values() method
print("\nPhone Numbers:")
for six_seven in contacts.values():
    print(f"-{six_seven}")
