def largest_mountain(arr):
    n = len(arr)
    max_height = 0  # To keep track of the largest mountain height

    for i in range(1, n - 1):  # We don't consider the first and last elements as they can't be peaks
        for h in range(arr[i], 0, -1):  # Start from current height and go down to 1
            left, right = i, i
            height = h

            if height < max_height:
                break  # we don't care about smaller mountains now
            # Traverse to the left to find the left side of the mountain
            current_height = h
            while left > 0 and current_height >= 1:
                if arr[left - 1] >= current_height - 1:
                    current_height -= 1
                    left -= 1
                else:
                    break

            # Traverse to the right to find the right side of the mountain
            current_height = h
            while right < n - 1 and current_height >= 1:
                if arr[right + 1] >= current_height - 1:
                    current_height -= 1
                    right += 1
                else:
                    break

            # Check if we have a valid mountain
            if left < i and right > i:
                max_height = max(max_height, height)

    return max_height


print(largest_mountain([0, 2, 2, 1, 3, 4, 2, 1, 0]))
print(largest_mountain([0, 0, 1, 2, 1, 0]))
print(largest_mountain([0, 4, 1]))
print(largest_mountain([0, 1, 3, 4, 1, 0]))

def largest_mountain_2(heights):
    max_mountain_height = 0  # Initialize the maximum mountain height to 0

    # Iterate through each index in the array
    for i in range(1, len(heights) - 1):
        for peak_height in range(heights[i], 0, -1):  # Try decreasing the height at index i

            left, right = i, i  # Initialize pointers for left and right traversal
            left_height, right_height = 1, 1  # Initialize the left and right mountain height to 1
            current_peak_height = peak_height  # Initialize the current peak height

            if peak_height < max_mountain_height:
                # is possible peak is less than max we can skip since we care only about max height
                continue
            # Move towards the left end to find the height of the left slope
            while left > 0 and current_peak_height > 1:
                if heights[left - 1] >= current_peak_height - 1:  # Mountain can extend
                    left_height += 1
                else:  # Mountain cannot extend, break
                    break
                current_peak_height -= 1
                left -= 1

            current_peak_height = peak_height  # Reset the current peak height for the right slope

            # Move towards the right end to find the height of the right slope
            while right < len(heights) - 1 and current_peak_height > 1:
                if heights[right + 1] >= current_peak_height - 1:  # Mountain can extend
                    right_height += 1
                else:  # Mountain cannot extend, break
                    break
                current_peak_height -= 1
                right += 1

            # The height of the mountain will be the minimum of left and right mountain heights
            mountain_height = min(left_height, right_height)

            # Update the maximum mountain height if the current mountain height is greater
            max_mountain_height = max(max_mountain_height, mountain_height)

    return max_mountain_height

print(largest_mountain_2([0, 2, 2, 1, 3, 4, 2, 1, 0]))
print(largest_mountain_2([0, 0, 1, 2, 1, 0]))
print(largest_mountain_2([0, 4, 1]))
print(largest_mountain_2([0, 1, 3, 4, 1, 0]))
def largest_mountain_dp(arr):
    n = len(arr)
    max_height = 0

    # Initialize arrays to store slopes
    left_slope = [0] * n
    right_slope = [0] * n

    # Calculate slopes from left to right
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            left_slope[i] = left_slope[i - 1] + 1

    # Calculate slopes from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            right_slope[i] = right_slope[i + 1] + 1

    # Find the tallest mountain
    for i in range(1, n - 1):
        left = left_slope[i]
        right = right_slope[i]

        # To form a mountain, both sides need at least one downslope
        if left == 0 or right == 0:
            continue

        # Height is determined by the minimum slope on either side, capped by the original height
        height = min(left, right, arr[i])

        # Update the maximum height
        max_height = max(max_height, height)

    return max_height

# # Test the function
# print(largest_mountain_dp([0, 2, 2, 1, 3, 4, 2, 1, 0]))  # Output should be 3
# print(largest_mountain_dp([0, 0, 1, 2, 1, 0]))  # Output should be 2
# print(largest_mountain_dp([0, 4, 1]))  # Output should be 1
# print(largest_mountain_dp([0, 1, 3, 4, 1, 0]))  # Output should be 2