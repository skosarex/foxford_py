def symbol_for_digit(value):
    if 0 <= value < 10:
        return chr(ord('0') + value)
    elif 10 <= value <= 36:
        return chr(ord('A') + value - 10)


number = int(input('Enter the number in decimal system: '))
base = int(input('Enter base: '))
number_in_base = ''
while number != 0:
    digit = number % base
    number_in_base = symbol_for_digit(digit) + number_in_base
    number = number // base

print(number_in_base)
