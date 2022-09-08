#    // in cpp and java,  use (ctrl+/)  to give the line comment

'''
  THIS IS MULTI LINE COMMENT: BUT DONT USE IT , BCZ IT IS USED FOR special purpose i.e, DOCUMENTATION
  when we click on some in-built methods, it shows us documentation
'''


"""
if u r creating any documentation then only use triple quotes.
dont write comments in triple quotes.
"""

"""
Is python Compiled or interpreted language?  ANS: It is both
in some books they said python is only interpreted language , now lets check

c & c++  are compiled languages bcz u as a programmer writes a c/c++ code. these r HIGH LEVEL language, means machine cant understand these 
languages. So, Compiler converts our c/c++ code into machine language(binary format). A Compiler can converts any language from any language
from HIGH TO HIGH as well. JAVA is an interpreted language.  IN PYTHON,

          SOURCE CODE -> COMPILER -> BYTE CODE -> INTERPRETER(PVM) -> MACHINE LANGUAGE
          
interpreter is Python Virtual Machine.

interpreted language means that ur interpreter will read each and every line 1-by-1 and it starts executing
line-by-line. and our Byte Code is interpreted. but, why we make it so complex: first compilation and then going for interpretation: for 1 reason.
We use the concept of byte code to achieve Portability. platform independence means u can write code once and then can run on different platforms.
Ex, as ur machine changes, ur cpu architecture also changes. So, if u r writing code for 1 machine and u compile it to get a binary file, then it 
may not work on some other machine bcz, machine may have different cpu architecture and to stop this problem we have this concept of virtual machine
NOW, in this virtual machine what we runs is a byte-code  and this code works on this virtual machine gets converted to machine code.

FOR PYTHON, we have PVM(python virtual machine), FOR JAVA: JVM, 

IN JAVA, first we compile the code by javac, and then run the file using java command.  javac Demo.java  -->  java Demo
In python, simply just:    python Demo.py   (we dont do compilation here and its the beauty of python)
python itself do all the task, BEHIND the scenes:python creates byte-code first and that byte-code gets run on PVM
    
pYthon is just a language , set of rules and conventions. and the actual implementation is CPYTHON and many others like PYPY,ironpython, jython
in cpython implementation is in c lang, jython internal implementation is done by java lang, .netversion is ironpython.... 
In general, the widely used implementation is cpython......................
"""