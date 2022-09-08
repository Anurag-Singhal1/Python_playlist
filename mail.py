# first, open ur gmail and turn on security access

import smtplib                           # smtp - simple mail transfer protocol

server = smtplib.SMTP('smtp.gmail.com',587)            #  server address and PORT NO.

server.starttls()                         # start the secure connection

server.login('anuragsinghal811@gmail.com','oectophiylzqqvty')                # generate app password
server.sendmail('anuragsinghal811@gmail.com','prashant.mishra2020@vitbhopal.ac.in','MAil sent from python code...now i m on the way to also become intelligent like u....thanks have a nice day')
print("Mail sent")
