##############################################################
#	
#	SOLITAIRE SOLVER
#	IST IA 18/19 - GROUP TP017 JOAO NEVES 83405, DIOGO REDIN 84711
#
##############################################################

import sys
from search import *

class sol_state():
	'''Represents a solitaire board.'''

	__slots__ = ['board']

	def __init__(self, board):
		self.board = board

	def get_board(self):
		return self.board

	def __lt__(self, otherState):
		return len(board_moves(self.get_board())) > len(board_moves(otherState.get_board()))

class solitaire(Problem):
	'''Models a Solitaire problem as a satisfaction problem.
	A solution can only have one piece left in the board.'''

	def __init__(self, board):
		super().__init__(sol_state(board))

	def actions(self, state):
		'''Returns all possible next states for the state we are in.'''
		return board_moves(state.get_board())

	def result(self, state, move):
		'''Applies a given move to the current board.'''
		return sol_state(board_perform_move(state.get_board(), move))

	def goal_test(self, state):
		'''Board is solved if it has only one piece left.'''
		return board_solved(state.get_board())

	def h(self, node):
		'''This heuristic prefers states that have more pegs closer to the 
		center. We sum the manhattan distance of all pegs to the center of the board -
		the higher this sum is, the further we are from the solution.'''

		# Board and size
		board = node.state.get_board()
		lines = len(board)
		columns = len(board[0])

		# Center
		mid_line = lines >> 1
		mid_column = columns >> 1

		# Accumulated cost
		cost = 0

		# Minimum cost so far
		minCost = sys.maxsize

		# Run board and for each peg accumulate their distance to the center
		for line in range(len(board)):
			for column in range(len(board[line])):

				pos = get_pos(board, make_pos(line, column))
				if(is_peg(pos)):

					# Manhattan distance
					cost += abs(column - mid_column) + abs(line - mid_line)

					# Save minimum
					if ( minCost > abs(column - mid_column) + abs(line - mid_line) ):
						minCost = abs(column - mid_column) + abs(line - mid_line)

		# If there is only one peg left heuristic should gcive 0 so we subtract the minimum cost (only one) so far
		return cost - minCost

##############################################################
#
#	CONTENT METHODS
#
##############################################################

def c_peg():
	return "O"

def c_empty():
	return "_"

def c_blocked():
	return "X"

def is_empty(e):
	return e == c_empty()

def is_peg(e):
	return e == c_peg()

def is_blocked(e):
	return e == c_blocked()

##############################################################
#
#	POSITION METHODS
#
##############################################################

# Makes a tuple position
def make_pos(l, c):
	return (l, c)

# Returns the position line
def pos_l(pos):
	return pos[0]

# Returns the position column
def pos_c(pos):
	return pos[1]

# Returns the content of the position "pos" of the board
def get_pos(board, pos):
	return board[pos_l(pos)][pos_c(pos)]

# Puts the content in the position "pos" of the board
def put_pos(board, pos, content):
	board[pos_l(pos)][pos_c(pos)] = content

# Returns the position between the two positions (if there is one)
def mid_pos(pos_i, pos_j):
	mid_line = (pos_l(pos_j) - pos_l(pos_i)) >> 1
	mid_column = (pos_c(pos_j) - pos_c(pos_i)) >> 1

	if (-1 <= mid_line <= 1) and (-1 <= mid_column <= 1):
		return make_pos(mid_line + pos_l(pos_i), mid_column + pos_c(pos_i))

##############################################################
#
#	MOVE METHODS ([p_initial, p_final])
#	p_initial and p_final are tuples
#
##############################################################

def make_move(i, f):
	return [i, f]

def move_initial(move):
	return move[0]

def move_final(move):
	return move[1]

##############################################################
#
#	BOARD SOLVED - Checks if the board is solved.
#
##############################################################

def board_solved(board):
	'''Given a board finds if the board is solved. The board is solved if it has only one peg.'''

	# Number of pegs in the board
	counter = 0

	for line in range (len(board)):
		for column in range (len(board[line])):

			pos = make_pos(line, column)
			if is_peg (get_pos(board, pos)):
				counter += 1
				if counter > 1:
					return False

	return True

##############################################################
#
#	BOARD MOVES - Function for the solitaire class.
#
##############################################################

def board_moves(board):
	'''Given a board finds all the ortogonal possible moves. It is returned as a list of moves.'''

	# Possible moves on the board
	moves = []

	for line in range(len(board)):
		for column in range(len(board[line])):

			# If the position contains a piece calculate possible moves here
			pos_initial = make_pos(line, column)
			if is_peg(get_pos(board, pos_initial)):

				if ( line < len(board) - 2):

					# Upward Movement
					pos_middle = make_pos(pos_l(pos_initial) + 1, pos_c(pos_initial))
					pos_final = make_pos(pos_l(pos_initial) + 2, pos_c(pos_initial))

					if ( is_peg(get_pos(board, pos_middle)) and is_empty(get_pos(board, pos_final)) ):
						upward = make_move(pos_initial, pos_final)
						moves.append(upward)

				if ( line > 1 ):

					# Downward Movement
					pos_middle = make_pos(pos_l(pos_initial) - 1, pos_c(pos_initial))
					pos_final = make_pos(pos_l(pos_initial) - 2, pos_c(pos_initial))

					if ( is_peg(get_pos(board, pos_middle)) and is_empty(get_pos(board, pos_final)) ):
						downward = make_move(pos_initial, pos_final)
						moves.append(downward)

				if ( column > 1 ):

					# Left Movement
					pos_middle = make_pos(pos_l(pos_initial), pos_c(pos_initial) - 1)
					pos_final = make_pos(pos_l(pos_initial), pos_c(pos_initial) - 2)

					if ( is_peg(get_pos(board, pos_middle)) and is_empty(get_pos(board, pos_final)) ):
						left = make_move(pos_initial, pos_final)
						moves.append(left)

				if ( column < len(board[line]) - 2 ):
					
					# Right Movement
					pos_middle = make_pos(pos_l(pos_initial), pos_c(pos_initial) + 1)
					pos_final = make_pos(pos_l(pos_initial), pos_c(pos_initial) + 2)

					if ( is_peg(get_pos(board, pos_middle)) and is_empty(get_pos(board, pos_final)) ):
						right = make_move(pos_initial, pos_final)
						moves.append(right)
	
	return moves

##############################################################
#
#	BOARD PERFORM MOVE - Function for the solitaire class.
#
##############################################################

def board_perform_move(board, move):
	'''Given a board and a move performs the move on the given board and returns the changed board.'''

	# Creating a copy of the board
	board_new = [board[i][:] for i in range(len(board))]

	# Movement Positions
	pos_initial = move_initial(move)
	pos_final = move_final(move)

	# Empty first position
	put_pos(board_new, pos_initial, c_empty())

	# Empty middle position
	pos_mid = mid_pos(pos_initial, pos_final)
	put_pos(board_new, pos_mid, c_empty())

	# Fill final position
	put_pos(board_new, pos_final, c_peg())

	return board_new