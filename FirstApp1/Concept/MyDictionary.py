
my_months_dictionary = {
"Jan" : "January",
"Feb": "February",
"Mar": "March",
"Jan":"April"      # Duplicate key can overwrite perivious value
}

print(my_months_dictionary)

print(my_months_dictionary.get("Mar"))

print(my_months_dictionary.get("Lov","Invalid key"))

print(my_months_dictionary.items())


