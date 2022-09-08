# ANURAG SINGHAL - 20BAI10309

n = int(input('Number up to which squares and cubes need to be found: '))

squares = [i**2 for i in range(1, n+1)]
cubes = [i**3 for i in range(1, n+1)]
multiples_of_2 = []

print('Squares: ', squares)
print('Cubes: ', cubes)

for i in range(0, n):
    if squares[i] % 2 == 0:
        multiples_of_2.append(squares[i])
    if cubes[i] % 2 == 0:
        multiples_of_2.append(cubes[i])

print('Multiples of 2: ', multiples_of_2)
