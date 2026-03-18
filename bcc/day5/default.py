# def cityName(city="nagpur"):
#    print("The city name is:", city)
# cityName("New York")
# cityName("Los Angeles")
# cityName("Chicago")
# cityName()

def cityName(*city):
    print("The city name is:", city)

cityName("New York", "Los Angeles", "Chicago")