def booking_at_hotel_cost(nights) -> int:
    """Returns cost of booking for certain nights"""
    return nights * 500


def plane_ride_cost(city) -> int:
    """Returns ticket cost to a certain city"""
    return cities[city]


def price_for_car_rent(days4rent) -> int:
    """Returns cost of car rent for certain days"""
    price_rent = 1000 * days4rent
    if days4rent > 3:
        return (1000 * days4rent) - 750
    elif days4rent > 7:
        return (1000 * days4rent) - 1500
    return price_rent


def trip_cost(city, days4rent, nights):
    """Returns total cost of travel: booking, tickets and car rent"""
    return booking_at_hotel_cost(nights) + price_for_car_rent(days4rent) + plane_ride_cost(city)


cities = {'Kyiv': 500,
          'Lviv': 700,
          'Odessa': 300,
          'Kharkiv': 450,
          'Rivne': 600}
print(trip_cost('Kyiv', 5, 12))
