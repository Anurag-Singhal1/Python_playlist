# import  spl_calc              # it imports the code from that file

# print(__name__)       # we will getting __main__


 # main is the starting point of execution   in cpp like int main()
# we can have 5, 10 modules in a project....main() is our 1st module
# first module name is always main, from here our code starts
#  __name__ basically gives the name of our file\module. if we run  __name__  inside that file\module, then it gives us main
# but, if we run after importing that file, then it gives us the name of that file


# print("spl_var says : "+__name__)


#------------------------NOW, ITS USE--------------------------------------------------------------------
# if there is some text that we want to print, if only it is our first module of a project:then we use main() func and writes the if cond.

def main():
    print("HELLO")
    print("WELCOME USER")
# main()
if __name__ == "__main__":
    main()