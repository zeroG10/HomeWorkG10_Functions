# Option with elif and else
def operations_on_numbers(number_1, number_2, number_3):
    if number_1 + number_2 > number_3:
        print('The life is beautiful!')
    elif number_1 + number_2 == number_3:
        print('Everything is normal.')
    else:
        print('This is not good.')


operations_on_numbers(10, 4, 11)
operations_on_numbers(5, 4, 9)
operations_on_numbers(2, 3, 9)


# Operation without elif
def operations_on_numbers(number_1, number_2, number_3):
    if number_1 + number_2 > number_3:
        print('The life is beautiful!')
    else:
        print('This is not good.')


operations_on_numbers(12, 2, 9)
operations_on_numbers(5, 4, 9)
operations_on_numbers(2, 4, 9)


# Operation without - input()
def operations_on_numbers():
    print("Enter numbers: ")
    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())
    if number_1 + number_2 > number_3:
        print('The life is beautiful!')
    else:
        print('This is not good.')


operations_on_numbers()