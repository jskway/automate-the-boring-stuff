def collatz(number):
    if number % 2 == 0:
        print(number // 2, sep='')
        return number // 2
    else:
        print(3 * number +1, sep='')
        return 3 * number + 1


def collatz_sequence():
    try:
        print('Enter an integer:')
        integer = int(input('>'))

        while integer != 1:
            integer = collatz(integer)
    except ValueError:
        print('Error: Please enter an integer')

collatz_sequence()