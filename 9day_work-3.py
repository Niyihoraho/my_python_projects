travel_log= [
    {
        "country":"france",
        "visits":12,
        "cities" : ["berlin","hamburg","stuttgart"]
    },
    {
        "country":"Rwanda",
        "visits":15,
        "cities" : ["kigali","musanze","kamembe"]
    }
    
]
countryy=input("add country name: "),
visitss=int(input("number of visitis: "))
citiess= input("Add city names (comma-separated): ").split(",")

def add_data(country,visits,cities):
    new_country={
            "country":country,
            "visits":visits,
            "cities" : cities
    }

    travel_log.append(new_country)
    
add_data(countryy,visitss,citiess)

for outkey in range(len(travel_log)):
    for innerkey in travel_log[outkey]:
        Value=travel_log[outkey][innerkey]
        print(f"{innerkey}: {Value}")
        

    