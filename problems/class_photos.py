def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    # Time O(nlogn) + O(n) > O(nlog(n))
    # Space O(1)
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    # 	if min(redShirtHeights) > max(blueShirtHeights):
    # 		return True

    # 	if min(blueShirtHeights) > max(redShirtHeights):
    # 		return True

    flag_red = False
    flag_blue = False

    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] > blueShirtHeights[i]:
            flag_red = True
        elif redShirtHeights[i] < blueShirtHeights[i]:
            flag_blue = True
        else:
            return False
        if flag_red == flag_blue == True:
            return False

    return True


if __name__ == '__main__':

    red = [5, 8, 1, 3, 4]
    blue = [6, 9, 2, 4, 5]
    print(classPhotos(red,blue ))
