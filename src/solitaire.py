from search import *

##############################################################
#
#	SOLITAIRE SOLVER
#
##############################################################

class sol_state():
	'''Represents a solitaire board.'''

	__slots__ = ('board')

	def __init__(self, board):
		self.board = board

	def get_board(self):
		return self.board

	def __lt__(self, other_state):
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

	# Make the specified move in the board
	# def result(self, state, move):
		# return sg_state(board_perform_move(state.get_board(), move))

	# def goal_test(self, state)
	# def path_cost(self, c, state1, action, state2)
	# def h(self, node)

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

				if ( line+1 < len(board) ):

					# Top
					if ( is_peg(board[line+1][column]) and is_empty(board[line+2][column]) ):
						top = make_move([line,column], [line+2, column])
						moves.append(top)

				if ( line-1 > 0 ):

					# Bottom
					if ( is_peg(board[line-1][column]) and is_empty(board[line-2][column]) ):
						bottom = make_move([line,column], [line-2, column])
						moves.append(bottom)

				if ( column-1 > 0 ):

					# Left
					if ( is_peg(board[line][column-1]) and is_empty(board[line][column-2]) ):
						left = make_move([line,column], [line, column-2])
						moves.append(left)

				if ( column+1 < len(board[line]) ):

					# Right
					if ( is_peg(board[line][column+1]) and is_empty(board[line][column+2]) ):
						right = make_move([line,column], [line, column+2])
						moves.append(right)
	
	return moves

##############################################################
#
#	BOARD PERFORM MOVE - Function for solitaire class
#
##############################################################

def board_perform_move(board, move):
	'''Given a board and a move performs the move on the given board and returns the changed board.'''

##############################################################
#
#	MAIN
#
##############################################################

if (__name__ == "__main__"):

	file = open("example1.in", "r")

	contents = file.read()
	length = len(contents)
	board = []
	row = []

	for i in range(length):
		if (contents.startswith("X",i, i+1)):
			row.append("X")
		if (contents.startswith("O", i, i+1)):
			row.append("O")
		if (contents.startswith("_",i, i+1)):
			row.append("_")
		if	(contents.startswith("],",i, i+2)):
			board.append(row)
			row = []
		if	(contents.startswith("]]",i, i+2)):
			board.append(row)

	print("Initial board:")
	print(board)

	print("Possible moves:")
	print(board_moves(board))