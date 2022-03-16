def sunsetViews(buildings, direction):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    index_list = []

    print(direction)
    if direction == "EAST":
        print("inside east")
        current_max = 0
        for i in range(len(buildings) - 1, -1, -1):
            if buildings[i] > current_max:
                index_list.insert(0, i)
                current_max = buildings[i]

    else:
        current_max = 0
        for i in range(len(buildings)):
            if buildings[i] > current_max:
                index_list.append(i)
                current_max = buildings[i]
    return index_list


buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"
print(sunsetViews(buildings, direction))
