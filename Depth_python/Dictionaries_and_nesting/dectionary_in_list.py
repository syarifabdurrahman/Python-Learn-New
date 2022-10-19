travel_log = [
{
    "country": "France",
    "cities_visits":["Paris","Lille","Dijon"],
    "total_visits":13
},
{
    "country": "Indonesia",
    "cities_visits":["Jakarta","Yogyakarta","Bandung"],
    "total_visits":5
},
]

def add_new_country(name_country,total_visits,city_visits):
    new_country = {
        "country": name_country,
        "cities_visits":city_visits,
        "total_visits":total_visits
    }
    travel_log.append(new_country)
    print(travel_log)
    print(f"You\'ve visited {new_country['total_visits']} times")
    print(f"You\'ve been to {new_country['cities_visits'][0]} and {new_country['cities_visits'][1]}  times")


add_new_country("Russia",2,["Moscow","Petersburg"])
