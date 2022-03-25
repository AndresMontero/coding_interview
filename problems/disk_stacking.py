def diskStacking(disks):
    # Write your code here.
    # Time O(n^2)
    # Space O(n)

    disks.sort(key=lambda x: x[2])
    sequences = [None for x in disks]
    heights = [x[2] for x in disks]
    max_height_idx = 0

    for i in range(1, len(disks)):
        curr_disk_idx = i
        for j in range(i):
            other_disk_idx = j
            if disks[other_disk_idx][0] < disks[curr_disk_idx][0] \
                    and disks[other_disk_idx][1] < disks[curr_disk_idx][1] \
                    and disks[other_disk_idx][2] < disks[curr_disk_idx][2]:
                if heights[j] + disks[curr_disk_idx][2] >= heights[i]:
                    heights[i] = heights[j] + disks[curr_disk_idx][2]
                    sequences[i] = j
        if heights[i] >= heights[max_height_idx]:
            max_height_idx = i

    curr_index = max_height_idx
    disk_sequence = []
    while curr_index is not None:
        disk_sequence.append(disks[curr_index])
        curr_index = sequences[curr_index]
    print(heights)
    print(heights[max_height_idx])
    print(sequences)
    print(disk_sequence.reverse())
    return disk_sequence


print(diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]))
