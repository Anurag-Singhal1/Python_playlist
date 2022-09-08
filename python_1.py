# ANURAG SINGHAL - 20BAI10309

l1 = [1, 2, 3]
l2 = [3, 1, 4]
l3 = []

for i in l1:
    for j in l2:
        if i != j:
            l3.append((i, j))

print(l3)
