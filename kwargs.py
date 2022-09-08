# def person(name, *data):     # this is simple variable length argument
#     print(name)
#     print(data)
#
# person('ANURAG SINGHAL', 21,'SHAMLI', 3245671890)     # but here, we dont know is shamli a city/state/country.


# now comes: keyword variable length arguments (args)
def person(name, **data):
    print(name)
    print(data)
    print()
    for i,j in data.items():
        print(i,j)

person('ANURAG SINGHAL', age=21,city='SHAMLI', mob=3245671890)

