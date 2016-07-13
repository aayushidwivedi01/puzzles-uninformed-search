############################################################
# CIS 521: Homework 2
############################################################

student_name = "Aayushi Dwivedi"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import random
from collections import deque
import copy
############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    ans = 1;
    for i in xrange(n):
        ans *= (n**2 - i);
    return ans;

def num_placements_one_per_row(n):
    ans = 1;
    for i in xrange(n):
        ans *= n * (n -i);
    return ans;

def n_queens_valid(board):
    if (len(board) == 1):
        return True;
    for (r1,c1) in enumerate(board):
        if c1 in board[r1+1:]:
            return False;
        for r2 in xrange(r1 + 1, len(board)):
            if abs(r1 - r2) == abs(c1-board[r2]):
                return False;
    return True;
        
def get_next_config(config, n):
    return [ config+[i] for i in xrange(n - 1, -1, -1)];
        
def n_queens_solutions(n):
    frontier = get_next_config([], n)
    while frontier:
        config  = frontier.pop();
        if (n_queens_valid(config)):
            if (len(config) == n):
                yield config;
            else:
                frontier.extend(get_next_config(config, n));
    
############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board;
        self.rows = len(board);
        if self.rows != 0:
            self.cols = len(board[0]); 
        else:
            self.cols = 0;

    def get_board(self):
        return self.board;

    def perform_move(self, row, col):
        if(row >= 0 and row < self.rows\
            and col >= 0 and col < self.cols):
            self.board[row][col] = not self.board[row][col];
            
            up = row - 1; down = row + 1; left = col - 1; right = col +1;
            
            #toggle left neighbor
            if (left >= 0):
                self.board[row][left] = not self.board[row][left];
            #toggle right neighbor
            if (right < self.cols):
                self.board[row][right] = not self.board[row][right];
            #toggle top neighbor
            if (up >= 0):
                self.board[up][col] = not self.board[up][col];
            #toggle bottom neighbor
            if (down < self.rows):
                self.board[down][col] = not self.board[down][col]; 
        return;

    def scramble(self):
        for row in xrange(len(self.board)):
            for col in xrange(len(self.board[0])):
                if (random.random() < 0.5):
                    self.perform_move(row, col);

    def is_solved(self):
       return not(any([any(row) for row in self.board]));  


    def copy(self):
        new_board = copy.deepcopy(self.board)
        return LightsOutPuzzle(new_board)

    def successors(self):
        for row in xrange(self.rows):
            for col in xrange(self.cols):
                move = (row, col);
                new_board = self.copy();
                new_board.perform_move(row, col);
                yield (move, new_board)
    
    def find_solution(self):
        if (self.is_solved()):
            return []
        frontier = deque([([], self)] ) 
        boards_in_frontier = [];
        explored = set(); 
        while frontier:
            move, config  = frontier.popleft();
            explored.add( tuple(tuple(row) for row in config.get_board()));
            for (new_move, new_config) in config.successors():
                solution = move + [new_move]
                if (new_config.is_solved()):
                    return solution;
                state = (solution, new_config)
                new_board = tuple(tuple(row) for row in new_config.get_board())
                if new_config.get_board() not in boards_in_frontier \
                and new_board not in explored:
                    frontier.append( state); 
                    boards_in_frontier.append(new_config.get_board());
        return None
def create_puzzle(rows, cols):
    return LightsOutPuzzle([[False for col in xrange(cols)] for row in xrange(rows)]);

############################################################
# Section 3: Linear Disk Movement
############################################################
def create_identical_disk(length, n):
    return [ True if i < n else False for i in xrange(length)];

def create_goal_identical(length, n):
    return [False if i < length - n else True for i in xrange(length)];

def identical_successors(puzzle, length):
    for loc in xrange(length):
        if not puzzle[loc]:
            continue;
        old_puzzle = puzzle[:]
        if loc + 1 < length and puzzle[loc +1] \
            and loc + 2 < length and not puzzle[loc + 2]:
            puzzle[loc], puzzle[loc +2] = puzzle[loc +2], puzzle[loc]
            yield ( (loc, loc + 2), puzzle);
            puzzle = old_puzzle[:]

        if loc + 1 < length and not puzzle[loc + 1]:
            puzzle[loc], puzzle[loc +1] = puzzle[loc +1], puzzle[loc]
            yield ( (loc, loc +1), puzzle);
            puzzle = old_puzzle[:]

#def is_solved(puzzle,l, n):
#    if all(puzzle[l - n:]) and not all(puzzle[:l - n] ):
#        return True
#    return False

def solve_identical_disks(length, n):
    puzzle = create_identical_disk(length, n);
    goal = create_goal_identical(length, n);
    if  length == 0 or puzzle == goal:
        return [];
    frontier = deque( [([], puzzle)] );
    configs_in_frontier = set();
    explored = set();
    while frontier:
        move, config  = frontier.popleft();
        explored.add(tuple(config));
        for (new_move, new_config) in identical_successors(config, length):
            solution = move + [new_move]
            if (puzzle == goal):
                return solution;
            state = (solution, new_config)
            
            if tuple(new_config) not in configs_in_frontier \
                and tuple(new_config) not in explored:
                frontier.append(state);
                configs_in_frontier.add(tuple(new_config));
    return None


def create_distinct_disks(l, n):
    return [ i + 1  if i < n else 0 for i in xrange(l)];

def create_goal_distinct(l,n):
    return [ 0 if i < l - n else l - i  for i in xrange(l)];

def distinct_successors(puzzle, length):
    for loc in xrange(length):
        if  not puzzle[loc]:
            continue;
        old_puzzle = puzzle[:];
        
        if loc + 1 < length and old_puzzle[loc +1] \
            and loc + 2 < length and not old_puzzle[loc + 2]:
            old_puzzle[loc], old_puzzle[loc + 2] = old_puzzle[loc + 2], old_puzzle[loc]
            yield ( (loc, loc + 2), old_puzzle);
            old_puzzle = puzzle[:]
        
        if loc + 1 < length and not old_puzzle[loc + 1] :
            old_puzzle[loc], old_puzzle[loc +1] = old_puzzle[loc +1], old_puzzle[loc]
            yield ( (loc, loc +1), old_puzzle);
            old_puzzle = puzzle[:]

        if loc - 1 >= 0 and old_puzzle[loc - 1] \
            and loc -  2 >= 0 and  not old_puzzle[loc - 2]:
            old_puzzle[loc - 2], old_puzzle[loc] = old_puzzle[loc], old_puzzle[loc - 2]
            yield ( (loc, loc -  2), old_puzzle);
            old_puzzle = puzzle[:]

        if loc - 1 >= 0 and not old_puzzle[loc - 1] :
            old_puzzle[loc - 1], old_puzzle[loc] = old_puzzle[loc], old_puzzle[loc - 1]
            yield ( (loc, loc - 1), old_puzzle);
            old_puzzle = puzzle[:]

def solve_distinct_disks(length, n):
    puzzle = create_distinct_disks(length, n);
    goal = create_goal_distinct(length, n);
    if length == 0 or puzzle == goal:
        return [];
    frontier = deque([([], puzzle)]);
    configs_in_frontier = set();
    explored = set();

    while frontier:
        move, config  = frontier.popleft();
        for (new_move, new_config) in distinct_successors(config, length):
            solution = move + [new_move]
            if (new_config == goal):
                return solution;
            state = (solution, new_config)

            if tuple(new_config) not in explored \
                and tuple(new_config) not in configs_in_frontier:
                frontier.append(state);
                configs_in_frontier.add(tuple(new_config));
    return None


############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
15
"""

feedback_question_2 = """
I took a while to figure out 1st problem.
Rest of the problems were similar after that. 
Lecture slides were helpful.
"""

feedback_question_3 = """
It was an interesting assignment. I liked 
all three problems.
"""
