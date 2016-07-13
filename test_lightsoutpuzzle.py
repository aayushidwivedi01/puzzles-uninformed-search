import homework2 as hw2
import unittest
import timeit

#Lights Out Puzzle
class TestLightsOut(unittest.TestCase):
	def test_init(self):
		board = [[True, False],[False, False]]
		puzzle = hw2.LightsOutPuzzle(board)
		self.assertEqual(board, puzzle.get_board())
		board = [[True, False], [False, True]]
		puzzle = hw2.LightsOutPuzzle(board)
		self.assertEqual(board, puzzle.get_board())
		board = [[True, True], [True, True]]
		puzzle = hw2.LightsOutPuzzle(board)
		self.assertEqual(board, puzzle.get_board())
		
	def test_create_puzzle(self):
		puzzle = hw2.create_puzzle(2,2)
		self.assertEqual(puzzle.get_board(), [[False, False], [False, False]])
		puzzle = hw2.create_puzzle(2,3)
		self.assertEqual(puzzle.get_board(), [[False, False, False],[False, False, False]])
		puzzle = hw2.create_puzzle(1,1)
		self.assertEqual(puzzle.get_board(), [[False]])
		puzzle = hw2.create_puzzle(1,0)
		self.assertEqual(puzzle.get_board(), [[]])
		puzzle = hw2.create_puzzle(0,0)
		self.assertEqual(puzzle.get_board(), [])
		
	def test_perform_move(self):
		puzzle = hw2.create_puzzle(2,2)
		puzzle.perform_move(0,0)
		self.assertEqual(puzzle.get_board(), [[True, True], [True, False]])
		puzzle = hw2.create_puzzle(3,3)
		puzzle.perform_move(0,0)
		self.assertEqual(puzzle.get_board(), [[True,  True,  False],[True,  False, False],[False, False, False]])
		puzzle = hw2.create_puzzle(3,3)
		puzzle.perform_move(1,1)
		self.assertEqual(puzzle.get_board(), [[False, True, False],[True,  True, True ],[False, True, False]])
		puzzle = hw2.create_puzzle(3,3)
		puzzle.perform_move(1,2)
		self.assertEqual(puzzle.get_board(), [[False, False, True],[False,  True, True ],[False, False, True]])
		
	def test_scramble(self):
		puzzle = hw2.create_puzzle(0,0)
		self.assertEqual(puzzle.get_board(), [])
		puzzle.scramble()
		self.assertEqual(puzzle.get_board(), [])
		
	def test_is_solved(self):
		board = [[True, False],[False, False]]
		puzzle = hw2.LightsOutPuzzle(board)
		self.assertFalse(puzzle.is_solved())
		board = [[False, False],[False, False]]
		puzzle = hw2.LightsOutPuzzle(board)
		self.assertTrue(puzzle.is_solved())
		board = [[True, True],[True, True]]
		puzzle = hw2.LightsOutPuzzle(board)
		self.assertFalse(puzzle.is_solved())
		
	def test_copy(self):
		puzzle = hw2.create_puzzle(2,2)
		newPuzzle = puzzle.copy()
		puzzle.perform_move(0,0)
		self.assertNotEqual(puzzle.get_board(), newPuzzle.get_board())
		puzzle = hw2.create_puzzle(3,3)
		newPuzzle = puzzle.copy()
		self.assertEqual(puzzle.get_board(), newPuzzle.get_board())
		
	def test_successors(self):
		puzzle = hw2.create_puzzle(2, 2)
		result = [((0, 0),[[True, True], [True, False]]), ((0, 1),[[True, True], [False, True]]), ((1, 0),[[True, False], [True, True]]), ((1, 1),[[False, True], [True, True]])]
		i=0
		for (move, new_p) in puzzle.successors():
			self.assertEqual((move, new_p.get_board()), result[i])
			i+=1
		result = [6, 12, 20, 30]
		j=0
		for i in range(2, 6):
			puzzle = hw2.create_puzzle(i, i + 1)
			self.assertEqual(len(list(puzzle.successors())), result[j])
			j+=1
	
	def test_find_solutions(self):
		puzzle = hw2.create_puzzle(2, 2)
		puzzle.perform_move(0,0)
		self.assertEqual(puzzle.find_solution(),[(0, 0)])
		puzzle = hw2.create_puzzle(2, 3)
		for row in range(2):
			for col in range(3):
				puzzle.perform_move(row, col)
		self.assertEqual(puzzle.find_solution(),[(0, 0), (0, 2)])
		puzzle = hw2.create_puzzle(4,4)
		puzzle.scramble()
		moves =  puzzle.find_solution()
		for row, col in moves:
			puzzle.perform_move(row, col)
		self.assertEqual(puzzle.get_board(), (hw2.create_puzzle(4,4)).get_board())
		b = [[False, False, False],[False, False, False]]
		b[0][0] = True
		puzzle = hw2.LightsOutPuzzle(b)
		self.assertEqual(puzzle.find_solution(),None)

		
	def test_timeit(self):
		count = 10
		t = timeit.Timer("puzzle.find_solution()", 'import homework2 as hw2; puzzle = hw2.create_puzzle(4,4); puzzle.scramble()')
		print 'LightsOut(4,4) avg time:'
		print t.timeit(10)/count
		
if __name__ == '__main__':
	unittest.main()
	
	
	