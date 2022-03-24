def waterArea(heights):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    left_tallest = [0] * len(heights)
    right_tallest = [0] * len(heights)
    water_areas = [0] * len(heights)

    for i in range(1, len(heights)):
        left_tallest[i] = max(heights[i - 1], left_tallest[i - 1])

    for i in range(len(heights) - 2, -1, -1):
        right_tallest[i] = max(heights[i + 1], right_tallest[i + 1])

    for i in range(len(water_areas)):
        min_height = min(left_tallest[i], right_tallest[i])
        if heights[i] < min_height:
            water_areas[i] = min_height - heights[i]

    print(left_tallest)
    print(right_tallest)
    print(sum(water_areas), water_areas)

    return sum(water_areas)


def waterArea_1(heights):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    if not heights: return 0

    left = 0
    right = len(heights) - 1
    max_left = heights[left]
    max_right = heights[right]

    total_water = 0
    while left < right:
        if max_left < max_right:
            left += 1
            total_water += max(0, max_left - heights[left])
            max_left = max(max_left, heights[left])

        else:
            right -= 1
            total_water += max(0, max_right - heights[right])
            max_right = max(max_right, heights[right])

    print(total_water)
    return total_water


print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
print(waterArea_1([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
