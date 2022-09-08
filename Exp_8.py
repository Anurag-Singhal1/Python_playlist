# ANURAG SINGHAL - 20BAI10309
from collections import Counter

f = open('text.txt', 'r')
contents = f.read()
print(contents)
contents = contents.replace(',', '')
contents = contents.replace('.', '')
contents = contents.lower()


c = Counter(contents.split(' '))
print()
print()
print('The five most frequent words in the text are: ')

a = sorted(c.items(), key=lambda item: (-item[1], item[0]))

count = 0

for i in a:
    print(f'{i[0]}: {c[i[0]]} times')
    count += 1
    if count == 5:
        break
