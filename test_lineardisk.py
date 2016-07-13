import homework2 as hw2
import unittest
import timeit

#Linear Disk Movement 
class TestLinearDisk(unittest.TestCase):
	def test_solve_identical_disks(self):
		self.assertEqual(hw2.solve_identical_disks(4,2), [(0, 2), (1, 3)])
		self.assertEqual(hw2.solve_identical_disks(5,2), [(0, 2), (1, 3), (2, 4)])
		self.assertEqual(hw2.solve_identical_disks(4,3), [(1, 3), (0, 1)])
		self.assertEqual(hw2.solve_identical_disks(5,3), [(1, 3), (0, 1), (2, 4), (1, 2)])
		self.assertEqual(hw2.solve_identical_disks(0,0), [])
		self.assertEqual(hw2.solve_identical_disks(5,5), [])
		self.assertEqual(hw2.solve_identical_disks(5,0), [])
		res = hw2.solve_identical_disks(8,7)
		print len(res)
		res = hw2.solve_identical_disks(10,5)
		print len(res)
		
	def test_solve_distinct_disks(self):
		self.assertEqual(hw2.solve_distinct_disks(4,2), [(0, 2), (2, 3), (1, 2)])
		self.assertEqual(hw2.solve_distinct_disks(5,2), [(0, 2), (1, 3), (2, 4)])
		self.assertEqual(hw2.solve_distinct_disks(4,3), [(1, 3), (0, 1), (2, 0), (3, 2), (1, 3),(0, 1)])
		self.assertEqual(hw2.solve_distinct_disks(5,3), [(1, 3), (2, 1), (0, 2), (2, 4), (1, 2)])
		self.assertEqual(hw2.solve_distinct_disks(0,0), [])
		self.assertEqual(hw2.solve_distinct_disks(5,5), None)
		self.assertEqual(hw2.solve_distinct_disks(5,0), [])
		res = hw2.solve_distinct_disks(8,7)
		print len(res)
		res = hw2.solve_distinct_disks(10,5)
		print len(res)
		
		
	def test_timeit(self):
		count = 10
		t = timeit.Timer("hw2.solve_distinct_disks(8,7)", 'import homework2 as hw2')
		print 'Distinct(8,7) avg time:'
		print t.timeit(10)/count
		t = timeit.Timer("hw2.solve_distinct_disks(10,5)", 'import homework2 as hw2')
		print 'Distinct(10,5) avg time:'
		print t.timeit(10)/count
		t = timeit.Timer("hw2.solve_identical_disks(8,7)", 'import homework2 as hw2')
		print 'Identical(8,7) avg time:'
		print t.timeit(10)/count
		t = timeit.Timer("hw2.solve_identical_disks(10,5)", 'import homework2 as hw2')
		print 'Identical(10,5) avg time:'
		print t.timeit(10)/count
		
if __name__ == '__main__':
	unittest.main()