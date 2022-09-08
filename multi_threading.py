# What is a thread: when we break-down a big task into small parts, each part will be called as thread.
# Multi-Tasking: cpu are like quadcore cpu, octa core cpu
# By Default, every execution has 1 thread, even if u not creating a thread by urself, u do have 1 thread >>>Main Thread
# thread se simultaneously 2 thread banake (Hello , hi) print karega
#now, how can we create 2 different threads : 1. simply make them a sub class of Thread,

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):       # jaan bhujke run() method hi liya hai, bcz thread class has inside a method run(), agar run ko chorke koi aur method banaoge to kaam nhi karega
        for i in range(3):
            print("Hello")
            sleep(1)           # to reduce the speed

class Hi(Thread):
    def run(self):
        for i in range(3):
            print("Hi")
            sleep(1)


t1 = Hello()             # object declare krne pr, sirf init() func wala hi print hota haii..
t2 = Hi()

t1.start()      # run() ki jagh start() bhi kaam kr jaayega, bcz thread class mein run & start in-built haii,start() likhte hi now we have 3 threads: main , t1 & t2
sleep(0.2)      # to stop the collision in cpu from 2 threads
t2.start()

t1.join()      # here, we r asking our main thread to wait until t1 and t2 joins(complete their work)
t2.join()      # so now, ab ye last mein print ho jaayega

print("Jai Shree Ram")     # which thread is responsible to print this...: MAIN THREAD, after t1 and t2, main prints this


# SO THE ADVANTAGE OF THREAD IS THAT: we can use multiple cores of cpu and execute things simultaneously