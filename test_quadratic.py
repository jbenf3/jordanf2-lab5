
import quadratic

def main():

    #Write some tests in the following form

    x1 , x2 = quadratic.find_roots(1,2,-15)
    assert x1==-3 and x2==5 or x1==5 and x2==-3

    #The "assert" keyword says to pass if the following expression
    #returns True and to error if the expression returns False
    #The "or" keyword in the expression is important because you 
    #don't know what order the roots will be returned in!

    #You could replace the assert with an if statement that will 
    #print some information if a test fails if you prefer that style

    #Write more tests below:







    #Have this as the last line in main()
    print "All tests have been run! Any errors have been shown above."



if __name__=="__main__":
    main()
