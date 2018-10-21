from solitaire import *
from search import *

problem1 = [["_","O","O","O","_"],["O","_","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]]
problem2 = [["O","O","O","X"],["O","O","O","O"],["O","_","O","O"],["O","O","O","O"]]
problem3 = [["O","O","O","X","X"],["O","O","O","O","O"],["O","_","O","_","O"],["O","O","O","O","O"]]
problem4 = [["O","O","O","X","X","X"],["O","_","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"]]

compare_searchers(problems=[solitaire(problem1),solitaire(problem2),solitaire(problem3),solitaire(problem4)],header=['Searcher', 'problem1', 'problem2', 'problem3', 'problem4'],searchers=[depth_first_graph_search,greedy_first_search,astar_search])