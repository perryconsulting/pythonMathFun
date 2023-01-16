def collatz(number):
    collatz_num_list = []
    while number != 1:
        collatz_num_list.append(number)
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = int((3 * number) + 1)
    collatz_num_list.append(1)
    collatz_num_list_length = len(collatz_num_list)
    collatz_highest_int = 1
    for num in collatz_num_list:
        if num > collatz_highest_int:
            collatz_highest_int = num
    print("The Collatz sequence was: " + str(collatz_num_list))
    print("The number of steps in the Collatz sequence was: " + str(collatz_num_list_length - 1))
    print("The highest integer in the Collatz sequence was: " + str(collatz_highest_int))


print("\nWelcome to Python Math Fun.")
print("\n1. Collatz Conjecture")
print("0. Exit")

user_selection = input("Enter your selection: ")
match int(user_selection):
    case 1:
        print(
            "\nYou chose the Collatz Conjecture. \n\nThe Collatz conjecture states that by beginning with any "
            "positive integer,")
        print("you will eventually reach the number 1 by doing the following:")
        print("If the number is even, divide it by two.")
        print("If the number is odd, multiply it by three and add one.")
        print("Take the result and use it as the next input in the sequence.\n\n")
        collatz_num = input("Please enter a positive integer: ")
        collatz(int(collatz_num))

    case 0:
        exit()
