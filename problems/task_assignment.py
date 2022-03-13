def taskAssignment(k, tasks):
    # Write your code here.

    task_indices = {}

    for ind, task in enumerate(tasks):
        if task in task_indices:
            task_indices[task].append(ind)
        else:
            task_indices[task] = [ind]

    tasks.sort()

    i = 0
    j = len(tasks) - 1
    pairs = []

    while i < j:
        pairs.append([task_indices[tasks[i]].pop(), task_indices[tasks[j]].pop()])
        i += 1
        j -= 1


    return pairs


if __name__ == "__main__":
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]
    print(taskAssignment(k, tasks))
