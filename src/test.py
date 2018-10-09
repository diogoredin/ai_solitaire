import sys
import ast
from solitaire import *

filename = sys.argv[1]
file = open(filename, 'r')

board = ast.literal_eval(file.read())
file.close()

def greedy_best_first_search(problem):
	best_first_graph_search(problem, problem.h)

compare_searchers(problems=[solitaire(board)],
header=['Searcher', filename], searchers=[
depth_first_graph_search,
#greedy_best_first_search,
astar_search
])
