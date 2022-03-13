def validStartingCity_2(distances, fuel, mpg):
    # Write your code here.
    # Time O(n)
    # Space O(1)

    miles_left = 0
    min_miles_left = 0
    min_city = 0

    for city in range(1, len(distances)):
        previous_distance = distances[city - 1]
        previous_fuel = fuel[city - 1]

        miles_left += mpg * previous_fuel - previous_distance

        if miles_left < min_miles_left:
            min_miles_left = miles_left
            min_city = city

    return min_city


def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    # Time O(n^2)
    # Space O(1)
    for start_city in range(len(distances)):
        miles_remaining = 0
        for current_city in range(start_city, start_city + len(distances)):
            if miles_remaining < 0:
                break
            current_city = current_city % len(distances)

            fuel_current_city = fuel[current_city]

            distance_to_next_city = distances[current_city]

            miles_remaining += fuel_current_city * mpg - distance_to_next_city

        if miles_remaining >= 0:
            return start_city

    return -1


if __name__ == "__main__":
    distances = [30, 25, 5, 100, 40]
    fuel = [3, 2, 1, 0, 4]
    mpg = 20
    print(validStartingCity(distances, fuel, mpg))
    print(validStartingCity_2(distances, fuel, mpg))
