# to save and store our data/game/info/anything, we use database....it can also be a single .txt file but we use RDBMS here
# to work with sql u have these 2 choices:    MYSQL WORKBENCH     AND       MYSQL SHELL
# in shell, we have to insert all the commands but if we want something like GUI where we just right click and we do stuff then, WORKBENCH
# the only reason why people dont prefer workbench is bcz may be it was loaden ur machine and may be they want more geek environment, so u can also use Shell
# But, we want to focus on mysql workbench
# the ultimate goal was to connect python with database : we need mysql connector for this
# if u want to connect mysql with ANY language , u need a connector in between

import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",passwd="123456")
mydb = mysql.connector.connect(host="localhost",user="root",passwd="123456",database="anurag")
mycursor = mydb.cursor()                           # imagine cursor as pointers, they  point to the particular locations
# mycursor.execute("show databases")                 # to execute any sql statement, simply use execute() method and simply write sql query in it
mycursor.execute("select * from student")                  # student is a table in "anurag" database
result = mycursor.fetchall()           # here, we r fetching data from cursor and putting that into result,and from result we r fetching the data
# result = mycursor.fetchone()              # to fetch only 1 record
for i in result:                          # prints in next line due to for loop
    print(i)

# for i in mycursor:
#     print(i)                                       # Now, we get all our databases from sql


