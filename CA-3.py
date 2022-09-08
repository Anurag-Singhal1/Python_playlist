A = []
r1 = int(input("Enter rows for matrix1: "))
c1 = int(input("Enter columns for matrix1: "))
print("Enter the elements: ")

for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    A.append(row)
print(A)

print("Display Array In Matrix Form")
for i in range(r1):
    for j in range(c1):
        print(A[i][j], end=" ")
    print()

B = []
r2 = int(input("Enter rows for matrix2: "))
c2 = int(input("Enter columns for matrix2: "))
print("Enter the element: ")

for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input()))
    B.append(row)
print(B)

print("Display Array In Matrix Form")
for i in range(r2):
    for j in range(c2):
        print(B[i][j], end=" ")
    print()

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            row.append(0)
        result.append(row)

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    print("The Resultant Matrix Is: ")
    for r in result:
        print(r)
