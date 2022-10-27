

numbers_letters = {
    "1": " ",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}


def generateWords(num):

    global numbers_letters

    first_four = num[0:4]
    six_letters = num[4:]

    letter_one = numbers_letters.get(six_letters[0])
    letter_two = numbers_letters.get(six_letters[1])
    letter_three = numbers_letters.get(six_letters[2])
    letter_four = numbers_letters.get(six_letters[3])
    letter_five = numbers_letters.get(six_letters[4])
    letter_six = numbers_letters.get(six_letters[5])

    print(letter_one)
    combination_count = 0
    for l_one in letter_one:
        for l_two in letter_two:
            for l_three in letter_three:
                for l_four in letter_four:
                    for l_five in letter_five:
                        for l_six in letter_six:
                            print("Number: " + str(first_four) + str(l_one) + str(l_two) + str(l_three) + str(l_four) + str(l_five) + str(l_six))
                            combination_count = combination_count + 1
    print("Total: " + str(combination_count))

while True:
    print("Key: 1 = , 2 = ABC, 3 = DEF, 4 = GHI, 5 = JHL, 6 = MNO, 7 = PQRS, 8 = TUV, 9 = WXYZ, 0 = ")
    user_input = input("Enter your desired 1300/1800 number, or X to exit")
    if user_input == 'X' or user_input == 'x':
        quit()

    if len(user_input) == 10:
        generateWords(user_input)
    else:
        print("Entered value not 10 digits")
