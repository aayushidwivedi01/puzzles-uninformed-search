import homework2 as hw2
import unittest
import timeit

#N Queens problem
class TestNQueens(unittest.TestCase):
	def test_num_placements_all(self):
		self.assertEqual(hw2.num_placements_all(1),1)
		self.assertEqual(hw2.num_placements_all(2),12)
		self.assertEqual(hw2.num_placements_all(3),504)
		#print hw2.num_placements_all(9)
		
	def test_num_placements_one_per_row(self):
		self.assertEqual(hw2.num_placements_one_per_row(1),1)
		self.assertEqual(hw2.num_placements_one_per_row(2),8)
		self.assertEqual(hw2.num_placements_one_per_row(3),162)
		#print hw2.num_placements_one_per_row(9)
		
	def test_n_queens_valid(self):
		self.assertEqual(hw2.n_queens_valid([0, 0]),False)
		self.assertEqual(hw2.n_queens_valid([0, 2]),True)
		self.assertEqual(hw2.n_queens_valid([0, 1]),False)
		self.assertEqual(hw2.n_queens_valid([0, 3, 1]),True)
		self.assertEqual(hw2.n_queens_valid([6, 4, 2, 0, 5, 7, 1, 3]),True)		
		self.assertEqual(hw2.n_queens_valid([6, 3, 2, 0, 5, 7, 1, 3]),False)	
		
	def test_n_queens_solutions(self):
		solutions = hw2.n_queens_solutions(4)
		self.assertEqual(next(solutions),[1, 3, 0, 2])
		self.assertEqual(next(solutions),[2, 0, 3, 1])
		solutions = list(hw2.n_queens_solutions(6))
		self.assertEqual(solutions, [[1, 3, 5, 0, 2, 4], [2, 5, 1, 4, 0, 3], [3, 0, 4, 1, 5, 2], [4, 2, 0, 5, 3, 1]])
		solutions = list(hw2.n_queens_solutions(8))
		self.assertEqual(len(solutions), 92)
		solutions = list(hw2.n_queens_solutions(9))
		self.assertEqual(len(solutions), 352)
		
	def test_timeit(self):
		count = 10
		t = timeit.Timer("hw2.n_queens_solutions(9)", 'import homework2 as hw2')
		print 'NQueens(9) avg time:'
		print t.timeit(10)/count
		
if __name__ == '__main__':
	unittest.main()
