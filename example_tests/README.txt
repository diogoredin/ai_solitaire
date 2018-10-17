
O que é que cada teste foca:

# Test 01 a 08 - board_moves

# Test 09 a 12 - board_perform_move

# Test 13 a 16 - sol_state
# Test 13 - create sol_state
# Test 14 - access board of sol_state
# Test 15,16 - compare states: < e >

# Test 17 a 32 - solitaire
# Test 17 - solitaire(board) type is solitaire
# Test 18 - solitaire.initial type is sol_state
# Test 19 - solitaire.initial.board

# Test 20 - solitaire.actions(initial.state)
# Test 21 - solitaire.actions(initial.state)

# Test 22 - solitaire.goal_test(initial.state)
# Test 23 - solitaire.goal_test(initial.state)
# Test 24 - solitaire.goal_test(initial.state)

# Test 25 - solitaire.result(board, action)
# Test 26 - solitaire.result(board, action)

# Test 27 - Depth First Search super simple with solution
# Test 28 - Depth First Search super simple with no solution
# Test 29 - Depth First Search 
# Test 30 - Greedy search 
# Test 31 - A* 
# Test 32 - A* 


São usadas as seguintes funções cujo código não foi publicado:

1) xx_invalid_solution(<board>, <result of search>)
   A função devolve False se o resultado da procura estiver correcto.
   Senão a função devolve uma mensagem de erro que tenta mostrar o que falhou.
   Por exemplo:
    - "A procura devia retornar um objecto do tipo Node e nao um do tipo <class 'int'> com valor 5"
    - "A accao 8 nao e valida <accao> A sequencia de accoes e: <seq de accoes>"
    - "O tabuleiro nao tem só um pino: <board>"
