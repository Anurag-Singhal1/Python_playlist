# associated files: anurag.jpeg , MyPic.jpg , abc , MyData  : we handle all these files here 

# to store data we find permanent storage, 1 way to do so is by using Relational Database like MYSQL, ORACLE..., but it also provides u a
# table structure, and those r complex stuff....so best way to store for longer time in simple format is TEXT FILE.
# but how to open external file in a code
# to read a file, we may achieve Multi-threading, but to write a file we have to make sure that we r using only 1 thread or something like that
# READ , WRITE , APPEND  ,  READ BINARY   , WRITE BINARY

f = open('MyData','r')         # r is to only read the file, we cant do any change in that
# print(f)                        # prints filename, mode , etc..
# print(f.read())            # to print all the data in the file
# print(f.readline(),end='')          # to print only 1st line, end='' : to print in same line
# print(f.readline())          # line space is coming bcz, udhar file mein bhi next line mein hai, and ye print bhi apne aap next line mein laata haii


f1= open('abc','w')       # w is to write the file and it automatically creates a file if not there
# f1= open('abc','a')         # a means append here, if we dont want to erase something and add further
# f1.write("Anurag Singhal ")
# f1.write("Something ")                   # but, after removing it, it also got erased from abc file
# f1.write("People")

# -----------------NOW, COPY EVERYTHING FROM MYDATA TO ABC-----------------------------------------------------------------------------
# first read everything from mydata, and then write everything in abc

for data in f:
    # print(data)            # to print here in console
    f1.write(data)           # to print in abc file, ab jo usme pehle se hoga wo remove ho jaaayega

#------------------------NOW, TO PRINT IMAGE HERE --------------------------------------------------------------------------
f2 = open('anurag.jpeg','rb')          # so, rb means READ BINARY
# for i in f2:
#     print(i)              # we get values of the image

f3 = open('MyPic.jpg','wb')
for i in f2:
    f3.write(i)               # now, i get a file MyPic which has my photo

# in Files, we have 2 different modes:         1. CHARACTER MODE                     2. BINARY MODE
# in simple file with data, character format
# but here, file is an image, we dont have characters inside image, we have numbers: BINARY FORMAT

