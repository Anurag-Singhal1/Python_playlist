# ANURAG SINGHAL - 20BAI10309

n = int(input('Enter the number of strings you would like to input: '))
lst = []

for i in range(n):
    x = input(f'String {i+1}: ')
    lst.append(x)

print()

for i in lst:
    print(i, end=', ')
