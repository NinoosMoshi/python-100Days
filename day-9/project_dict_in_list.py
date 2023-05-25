travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# TODO: Write the function that will allow new countries
def add_new_country(country_visited, time_visited, cities_visited):
    my_dictionary = {}
    my_dictionary["country"] = country_visited
    my_dictionary["visits"] = time_visited
    my_dictionary["cities"] = cities_visited
    travel_log.append(my_dictionary)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
