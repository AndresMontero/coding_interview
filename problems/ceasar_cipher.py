def caesarCipherEncryptor(string, key):
    # Write your code here.

    shift = key % 26
    result = []
    for s in string:
        asci = ord(s)
        if asci + shift <= 122:
            result.append(chr(asci + shift))
        else:
            result.append(chr(96 + (asci + shift) % 122))

    return ''.join(result)


if __name__ == '__main__':
    print(caesarCipherEncryptor("abcdcba", 65))
