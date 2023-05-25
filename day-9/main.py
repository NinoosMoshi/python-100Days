# my_dictionary = {
#     "city": "niles",
#     "code": "60714"
# }

# retrieving from dictionary
# print(my_dictionary["code"])

# add to dictionary
# my_dictionary["street"] = "9025 n chester"
# print(my_dictionary)

# empty dictionary
# empty_dictionary = {}

# edit dictionary
# my_dictionary["city"] = "morton grove"
# print(my_dictionary)

# for loop
# for key in my_dictionary:
#     print(key)   # will print keys
#     print(my_dictionary[key])  # will print values


# nested dictionary

# my_dictionary = {
#                  "key1": [list],
#                  "key2": {dict}
#                 }


# nested dictionary in a list
my_list = [
    {
        "name": "ninos",
        "car": ["crv", "mar cedes", "rav4"]
    },
    {
        "last": "moshi"
    }
]

print(my_list[0]["name"])

