import homework2 as hw2



def test_n_queens_solutions():
        solutions = list(hw2.n_queens_solutions(9))
        print len(solutions)


import timeit 
t = timeit.Timer("test_n_queens_solutions()", setup = "from __main__ import test_n_queens_solutions")
print t.timeit(number = 2)
