print('x\ty\tx and y')
print('-----------------------')
for x in False, True:
    for y in False, True:
        print(x, y, x and y, sep='\t')

print()

print('x\ty\tx or y')
print('-----------------------')
for x in False, True:
    for y in False, True:
        print(x, y, x or y, sep='\t')
