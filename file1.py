# import numpy                       # never ever save the file_name with the module names
# print(numpy.__version__)

import sys
# print(sys.path)           # this is how we search for our module in these paths

import file2               # this is a gud practice and not the below one
# from file2 import a
print(file2.a)
file2.printjoke("This is me")
