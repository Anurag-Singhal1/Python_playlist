# it connects multiple components: like to combine 2 lists

names = ("Anurag","Khushi","pranav")           # tuples
comps = ("Apple","Microsoft","Tesla")

# zipped = list(zip(names,comps))             #  also can write list/set/dict here instead of print


zipped = zip(names,comps)
# print(list(zipped))
# print(dict(zipped))
# print(set(zipped))          # just order shufffles and prints unique
for (a,b) in zipped:
    print(a,b)

# print(zipped)                    # it gives zip object address