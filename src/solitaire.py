from search import *

##############################################################
#
#	SOLITAIRE SOLVER
#
##############################################################

class sol_state():
	'''Represents a solitaire board.'''

	__slots__ = ('board',)

	def __init__(self, board):
		self.board = board

	def get_board(self):
		return self.board

	def __lt__(self, otherState):
		return 0

class solitaire(Problem):
	'''Models a Solitaire problem as a satisfaction problem.
		A solution can only have one piece left in the board.'''

	# State of the board
	def __init__(self, board):
		super().__init__(sol_state(board))

	# Retrieves a list of possible actions for the current board
	def actions(self, state):
		actions = list(filter(lambda x: len(x) > 1, board_moves(state.get_board())))
		return actions

	# Make the specified move in the bdioard
	def result(self, state, move):
		return sol_state(board_perform_move(state.get_board(), move))

	# Return true if we reached our goal
	def goal_test(self, state):
		return board_solved(state.get_board())

	# Heuristic (number of nodes available)
	def h(self, peg):
		return len(board_moves(peg.state.get_board()))

	# Path cost
	# def path_cost(self, c, state1, action, state2)

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

def make_pos(l, c):
	return (l, c)

def pos_l(pos):
	return pos[0]

def pos_c(pos):
	return pos[1]

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
	'''Given a board finds if the board is solved.'''

	# Iterate the board
	for line in range(len(board)):
		for column in range(len(board[line])):

			counter = 0
			if is_peg(board[line][column]):
				counter += 1
				if counter > 1:
					return False

	return True

##############################################################
#
#	BOARD MOVES - Function for solitaire class
#
##############################################################

def board_moves(board):
	'''Given a board finds all the ortogonal possible moves. It is returned as a list of moves.'''

	# Possible moves on the board
	moves = []

	# Iterate the board
	for line in range(len(board)):
		for column in range(len(board[line])):

			# If the position contains a piece calculate possible moves here
			if is_peg(board[line][column]):

				if ( line+2 < len(board) ):

					# Top
					if ( is_peg(board[line+1][column]) and is_empty(board[line+2][column]) ):
						top = make_move(make_pos(line,column), make_pos(line+2, column))
						moves.append(top)

				if ( line-1 > 0 ):

					# Bottom
					if ( is_peg(board[line-1][column]) and is_empty(board[line-2][column]) ):
						bottom = make_move(make_pos(line,column), make_pos(line-2, column))
						moves.append(bottom)

				if ( column-1 > 0 ):

					# Left
					if ( is_peg(board[line][column-1]) and is_empty(board[line][column-2]) ):
						left = make_move(make_pos(line,column), make_pos(line, column-2))
						moves.append(left)

				if ( column+2 < len(board[line]) ):

					# Right
					if ( is_peg(board[line][column+1]) and is_empty(board[line][column+2]) ):
						right = make_move(make_pos(line,column), make_pos(line, column+2))
						moves.append(right)
	
	return moves

##############################################################
#
#	BOARD PERFORM MOVE - Function for solitaire class
#
##############################################################

def board_perform_move(board, move):
	'''Given a board and a move performs the move on the given board and returns the changed board.'''

	# Initial
	initial = move_initial(move)
	final = move_final(move)

	# Empty first position
	line = pos_l(initial)
	column = pos_c(initial)
	board[line][column] = c_empty()

	# Empty middle position
	mid_line = int((pos_l(final) - pos_l(initial)) / 2)
	mid_column = int((pos_c(final) - pos_c(initial)) / 2)
	mid_pos = make_pos(mid_line + pos_l(initial), mid_column + pos_c(initial))
	board[pos_l(mid_pos)][pos_c(mid_pos)] = c_empty()

	# Fill final piece
	line = pos_l(final)
	column = pos_c(final)
	board[line][column] = c_peg()

	print("Possible moves:")
	return board