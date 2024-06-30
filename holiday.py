# Provide city options
def city_options():
    print("Please chose a city destination from the following:")
    print("ny = New York")
    print("la = Los Angeles")
    print("ln = London")
    print("ps = Paris")
    print("q = quit")


print("Let's plan your vacation!")
city_options()

# Request user input
city_flight = input("Chosen destination: ")
num_nights = int(input("How many nights would you like to stay? "))
rental_days = int(input("How many days will you be hiring car? "))

# Define 4 functions
def hotel_cost(num_nights):
    hotel_total = num_nights * 99
    return hotel_total


def plane_cost(city_flight):
    if city_flight == "ny":
        flight_cost = num_nights * 200
    elif city_flight == "la":
        flight_cost = num_nights * 215
    elif city_flight == "ln":
        flight_cost = num_nights * 150
    elif city_flight == "ps":
        flight_cost = num_nights * 140
    else:
        print("Invalid destination. Please try again.")
        return None
    return flight_cost


def car_rental(rental_days):
    car_total = rental_days * 150
    return car_total


def holiday_cost(hotel_cost, plane_cost, car_rental):
    if plane_cost is None:
        return None
    holiday_total = hotel_cost + plane_cost + car_rental
    return holiday_total


# Calculate and print the total cost
hotel_cost_amount = hotel_cost(num_nights)
plane_cost_amount = plane_cost(city_flight)
car_rental_amount = car_rental(rental_days)
total_cost = holiday_cost(hotel_cost_amount, plane_cost_amount, car_rental_amount)

if total_cost is not None:
    print(f"\nThe total vacation cost to {city_flight.upper()}")
    print(f"Staying for {num_nights} nights")
    print(f"With {rental_days} days car hire:")
    print(f"Hotel Cost: £{hotel_cost_amount}")
    print(f"Plane Cost: £{plane_cost_amount}")
    print(f"Car Rental Cost: £{car_rental_amount}")
    print(f"Total Cost: £{total_cost}")
else:
    print("Invalid destination. Unable to calculate the total cost.")




