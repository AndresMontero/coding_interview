def runLengthEncoding(string):
    # Write your code here.
    result = []

    i = 1
    size = len(string) - 1

    if len(string) == 1:
        return f'1{string[0]}'
    counter = 1
    while i <= size:
        if string[i] != string[i - 1] and counter > 0:
            result.append(f'{counter}{string[i - 1]}')
            counter = 1
        else:
            counter += 1
            if counter == 9:
                result.append(f'{counter}{string[i]}')
                counter = 0
        if i == size:
            result.append(f'{counter}{string[i]}')
        i += 1

    return ''.join(result)


if __name__ == '__main__':
    print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
