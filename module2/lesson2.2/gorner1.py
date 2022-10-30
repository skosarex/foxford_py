def digit_value(symbol):
    symbol = symbol.lower()
    if '0' <= symbol <= '9':
        return ord(symbol) - ord('0')
    elif 'a' <= symbol <= 'z':
        return 10 + ord(symbol) - ord('a')
    else:
        return 0


base = int(input('Enter base: '))
number = input('Enter the number: ')
x = 0
for digit in number:
    x = x * base + digit_value(digit)
print(x)
