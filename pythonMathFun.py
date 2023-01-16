def collatz(number):
    collatz_num_list = []
    while number != 1:
        collatz_num_list.append(number)
        if number % 2 == 0:
            number = number // 2
        else:
            number = (3 * number) + 1
    collatz_num_list.append(1)
    collatz_num_list_length = len(collatz_num_list)
    collatz_highest_int = 1
    for num in collatz_num_list:
        if num > collatz_highest_int:
            collatz_highest_int = num
    print("The Collatz sequence was: " + str(collatz_num_list))
    print("The number of steps in the Collatz sequence was: " + str(collatz_num_list_length - 1))
    print("The highest integer in the Collatz sequence was: " + str(collatz_highest_int))


def fibonacci_sequence_printer(number):
    if number <= 1:
        return number
    else:
        return fibonacci_sequence_printer(number - 1) + fibonacci_sequence_printer(number - 2)


def greatest_common_divisor_calculator(number1, number2):
    if number1 == 0:
        return number2
    return greatest_common_divisor_calculator(number2 % number1, number1)


def least_common_multiple_calculator(number1, number2):
    return (number1 // greatest_common_divisor_calculator(number1, number2)) * number2

print("\nWelcome to Python Math Fun.")
print("\n1. Collatz Conjecture")
print("2. Print a Fibonacci Sequence")
print("3. Find the Least Common Multiple of Two Integers")
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
    case 2:
        print(
            "\nYou chose a Fibonacci Sequence. \n\nEach number in the sequence is the sum of the two numbers that "
            "precede it.\n\n")
        fibonacci_sequence_length = input("How many numbers in the sequence would you like to display? ")
        fibonacci_sequence_list = []
        for i in range(int(fibonacci_sequence_length)):
            fibonacci_sequence_list.append(fibonacci_sequence_printer(i))
        print(str(fibonacci_sequence_list))
    case 3:
        print("\nYou chose the LCM calculator. \nThe Least Common Multiple is defined as the smallest number that "
              "can be divided by both integers provided.\n\n")
        lcm_number1 = input("Please enter the first integer: ")
        lcm_number2 = input("Please enter the second integer: ")
        greatest_common_divisor = greatest_common_divisor_calculator(int(lcm_number1), int(lcm_number2))
        print("\nGreat! First we have to find the Greatest Common Divisor: " + str(greatest_common_divisor))
        print("\nThe Least Common Multiple of " + str(lcm_number1) + " and " + str(lcm_number2) + " is: " + str(least_common_multiple_calculator(int(lcm_number1), int(lcm_number2))))
    case 0:
        exit()