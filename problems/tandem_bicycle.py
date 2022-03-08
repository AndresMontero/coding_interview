def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    # Time O(nlog(n))
    # Space O(1)
    if fastest:
        redShirtSpeeds.sort(reverse=True)
        blueShirtSpeeds.sort()
        total_speed = 0
        for i in range(len(redShirtSpeeds)):
            total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        total_speed = 0
        for i in range(len(redShirtSpeeds)):
            total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return total_speed


if __name__ == '__main__':
    red = [5, 5, 3, 9, 2]
    blue = [3, 6, 7, 2, 1]
    print(tandemBicycle(red, blue, True))
