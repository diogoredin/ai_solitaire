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

	# TODO less than method used for A* and other methods
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

# Returns the content of the position "pos" of the board
def get_pos(board, pos):
	return board[pos_l(pos)][pos_c(pos)]

# Puts the content in the position "pos" of the board
def put_pos(board, pos, content):
	board[pos_l(pos)][pos_c(pos)] = content

# Returns the position between the two positions (if there is one)
def mid_pos(pos_i, pos_j):
	mid_line = int((pos_l(pos_j) - pos_l(pos_i)) / 2)
	mid_column = int((pos_c(pos_j) - pos_c(pos_j)) / 2)

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
	'''Given a board finds if the board is solved.'''

	# Counter
	counter = 0

	# Iterate the board
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

					pos_middle = make_pos(pos_l(pos_initial), pos_c(pos_initial) + 1)
					pos_final = make_pos(pos_l(pos_initial), pos_c(pos_initial) + 2)

					# Right Movement
					if ( is_peg(get_pos(board, pos_middle)) and is_empty(get_pos(board, pos_final)) ):
						right = make_move(pos_initial, pos_final)
						moves.append(right)
	
	return moves

##############################################################
#
#	BOARD PERFORM MOVE - Function for solitaire class
#
##############################################################

def board_perform_move(board, move):
	'''Given a board and a move performs the move on the given board and returns the changed board.'''

	# Movement Positions
	pos_initial = move_initial(move)
	pos_final = move_final(move)

	# Empty first position
	put_pos(board, pos_initial, c_empty())

	# Empty middle position
	pos_mid = mid_pos(pos_initial, pos_final)
	put_pos(board, pos_mid, c_empty())

	# Fill pos_final piece
	put_pos(board, pos_final, c_peg())

	return board
