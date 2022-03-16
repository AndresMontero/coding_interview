def is_valid(string):
    if int(string) > 255:
        return False
    return len(string) == len(str(int(string)))


def validIPAddresses(string):
    # Write your code here.
    # Time O(1) does not deppend on the input size and is upperbound by 2^32
    # Space O(1) contant space
    ips_found = []

    for i in range(1, min(len(string), 4)):
        current_ip_parts = ['', '', '', '']

        current_ip_parts[0] = string[:i]
        if not is_valid(current_ip_parts[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            current_ip_parts[1] = string[i:j]
            if not is_valid(current_ip_parts[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                current_ip_parts[2] = string[j: k]
                current_ip_parts[3] = string[k:]
                if is_valid(current_ip_parts[2]) and is_valid(current_ip_parts[3]):
                    ips_found.append('.'.join(current_ip_parts))

    return ips_found


input = "1921680"
print(validIPAddresses(input))
