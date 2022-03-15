DIGIT_LETTERS = {'0': ['0'],
                 '1': ['1'],
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z'],

                 }


def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    # Time O(4^n * n)
    # Space O(4^n * n)
    current_nemonic = ['0'] * len(phoneNumber)
    nemonics_found = []

    nemonics_helper(0, phoneNumber, current_nemonic, nemonics_found)

    return nemonics_found


def nemonics_helper(idx, phone_number, current_nemonic, nemonics_found):
    if idx == len(phone_number):
        nemonics_found.append(''.join(current_nemonic))
    else:
        digit = phone_number[idx]
        letters = DIGIT_LETTERS[digit]

        for letter in letters:
            current_nemonic[idx] = letter
            nemonics_helper(idx + 1, phone_number, current_nemonic, nemonics_found)


if __name__ == "__main__":
    phoneNumber = "1905"
    print(phoneNumberMnemonics(phoneNumber))
