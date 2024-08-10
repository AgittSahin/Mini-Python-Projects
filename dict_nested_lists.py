captials = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary
"""
travel_log = {
    "France": ["Paris", "Lille", "Djon"],
    "Germany": ["Berlin", "Hamburg", "Munich"]    
}
"""

# Print Lille
""" print(travel_log["France"][1]) """

nested_list = ["A", "B", ["C", "D"]]

# Print "D"
""" print(nested_list[2][1]) """

travel_log = {
    "France":  {
        "visited_cities": ["Paris", "Lille", "Djon"],
        "total_visits": 8
    },
    "Germany": {
        "visited_cities": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5       
    },
}

print(travel_log["Germany"]["visited_cities"][2])
