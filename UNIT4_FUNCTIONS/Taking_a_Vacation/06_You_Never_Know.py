def hotel_cost(nights):
      return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475

def rental_car_cost(days):
    tickets = 40 * days
    if days >= 7:
        tickets -= 50
    if days >= 3:
        tickets -= 20
    return tickets

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

def double(n):
    return 2 * n
def triple(p):
    return 3 * p

def nights(a, b):
    return double(n) + triple(p)
