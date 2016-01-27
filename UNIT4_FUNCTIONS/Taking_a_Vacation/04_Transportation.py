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
