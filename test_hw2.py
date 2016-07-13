import homework2 as hw  # this imports our code in example.py, assuming it is in the same directory
import unittest


class TestProblem1(unittest.TestCase):
    def test_num_placements_all(self):
        print "PROD:{}".format(hw.num_placements_all(3))

    def test_num_placements_one_per_row(self):
        self.assertEqual(hw.num_placements_one_per_row(2), 8)
        self.assertEqual(hw.num_placements_one_per_row(3), 162)
        self.assertEqual(hw.num_placements_one_per_row(5), 375000)

    def test_n_queens_valid(self):
        l = [0,0]
    
        self.assertFalse(hw.n_queens_valid(l))
        self.assertTrue(hw.n_queens_valid([0,2]))
        self.assertFalse(hw.n_queens_valid([0, 1]))
        self.assertTrue(hw.n_queens_valid([0, 3, 1]))
        self.assertTrue(hw.n_queens_valid([6,4,2,0,5,7,1,3]))

    def test_n_queens_solutions(self):
        solutions = list(hw.n_queens_solutions(6));
        for solution in solutions:
            print solution
        print "Total:{}".format(len(list(solutions)))

class TestProblem2(unittest.TestCase):
        
    def test_init(self):
        board = [[False, False],[True, True]]
        lights = hw.LightsOutPuzzle(board);
        self.assertEqual(lights.get_board(), board)

    def test_create_puzzle(self):
        p = hw.create_puzzle(2,3)
        self.assertEquals(p.get_board(),\
             [[False, False, False], [False, False, False]])

    def test_perform_move(self):
        p  = hw.create_puzzle(3, 3)
        p.perform_move(1, 1)
        self.assertEquals( p.get_board(), [[False, True, False],\
                                [True,  True, True ],\
                                [False, True, False]])

        p2  = hw.create_puzzle(3, 3)
        p2.perform_move(0, 0)
        self.assertEquals( p2.get_board(),[[True,  True,  False],\
                    [True,  False, False],\
                    [False, False, False]])
    def test_scramble(self):
        p = hw.create_puzzle(3,3)
        p.scramble();
        print p.get_board()
    
    def test_is_solved(self):
        p = hw.create_puzzle(3,3)
        self.assertTrue(p.is_solved())       

        b = [[True,True], [False, True]]
        p = hw.LightsOutPuzzle(b)
        self.assertFalse(p.is_solved())

    def test_successors(self):
        p = hw.create_puzzle(2, 2)
        for move, new_p in p.successors():
            print move, new_p.get_board()

        for i in range(2, 6):
            p = hw.create_puzzle(i, i + 1);
            print len(list(p.successors()))

    def test_find_solution(self):
        p = hw.create_puzzle(2, 3)
        for row in range(2):
            for col in range(3):
                p.perform_move(row, col)
        self.assertEqual(p.find_solution(), [(0, 0), (0, 2)])

class TestProblem3(unittest.TestCase):
    def test_is_solved(self):
        t = [True, True, False, False];
        self.assertFalse(hw.is_solved(t, 4, 2));

        t2 = [False, True, True]
        self.assertTrue(hw.is_solved(t2, 3,2));

    def test_solve_identical_disks(self):
        p = hw.solve_identical_disks(4, 2);
        self.assertEqual(p, [(0, 2), (1, 3)]);

        p = hw.solve_identical_disks(5, 2);
        self.assertEqual(p, [(0, 2), (1, 3), (2, 4)]);
        
        p = hw.solve_identical_disks(4, 3);
        self.assertEqual(p , [(1, 3), (0, 1)]);
        
        p = hw.solve_identical_disks(5, 3);
        self.assertEqual(p , [(1, 3), (0, 1), (2, 4), (1, 2)]);
    
    def test_create_distince_disks(self):
        p = hw.create_distinct_disks(5,3);
        self.assertEqual(p, [ 1, 2, 3, 0, 0]);

    def test_create_goal(self):
        p = hw.create_goal(5, 3)
        self.assertEqual(p, [0, 0, 3, 2, 1]);
    
    def test_solve_distinct_disks(self):
        p = hw.solve_distinct_disks(4, 2);
        self.assertEqual(p, [(0, 2), (2, 3), (1, 2)]);
        p = hw.solve_distinct_disks(4, 3);    
        self.assertEqual(p, [(1, 3), (0, 1), (2, 0), (3, 2), (1, 3),(0, 1)]);

        p = hw.solve_distinct_disks(10, 5);
        #self.assertEqual(p, [(1, 3), (2, 1), (0, 2), (2, 4), (1, 2)]);
        print len(p)
if __name__ == '__main__':
    unittest.main()


