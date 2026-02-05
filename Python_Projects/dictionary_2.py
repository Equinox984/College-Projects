# Creating a Dictionary
country_capitals = {"Germany": "Berlín", "Canada": "Ottawa", "England": "London"}

country_capitals["Paraguay"] = "Asunción"
country_capitals["Guyana"] = "Georgetown"
country_capitals["Trinidad y Tobago"] = "Port of Spain"
country_capitals["Chile"] = "Santiago"
country_capitals["Nicaragua"] = "Managua"
country_capitals["Ecuador"] = "Quito"
country_capitals["Bahamas"] = "Nassau"

print(country_capitals, "\n")

# Delete Countries
del country_capitals["Germany"]
del country_capitals["Chile"]
print(country_capitals, "\n")

# Remove Everything
# country_capitals.clear()
# print(country_capitals)

# Countries Listing
for six_seven in country_capitals:
    print(f"I want to visit -> {six_seven}")
    print(f"And I want to go to the capital city -> {country_capitals[six_seven]}\n")
