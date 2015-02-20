
import analysis


def main():

    #Example test using testData1.dat
    data = analysis.load("testData1.dat")
    max_y_index = analysis.max_y_index(data)
    assert max_y_index == 5


    #Write more tests, which load your own short data files
    #And be sure to test both your max_y_index() and find_peak() functions



    #Have this as the last line in main()
    print "All tests have been run! Any errors have been shown above."






if __name__=="__main__":
    main()
