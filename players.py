'''
    Defines Player class, and subclasses Human and Minimax Player.
'''
import time 

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        print('Available Moves: ', board.num_legal_moves_remaining(self.symbol))
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
        self.time = 0
        self.time_end = 0
        self.total_time = 0
        self.num_moves = 0
    
    def clone(self):
        opp = MinimaxPlayer(self.oppSym)
        return opp

    def utility(self, board):
        game_result = 0
        score = board.count_score(self.symbol)
        if score > board.count_score(self.oppSym):
            game_result = 1 # victory
        if score < board.count_score(self.oppSym):
            game_result = -1 # defeat
        if score == board.count_score(self.oppSym):
            game_result == 0 # tie
        return game_result

    def successor(self, board):
        available_moves = board.num_legal_moves_remaining(self.symbol)
        return available_moves

# function MINIMAX-SEARCH(game, state) returns an action 
    # player <- game.To-MOVE(state)
    # value, move <- MAX-VALUE(game, state)
    # return move
    def minimax_search(self, board, depth):
        value, move = self.max_value(board, depth)
        print(value)
        print("Best Move Using MINIMAX: ", move)
        return move

    def max_value(self, board, depth):
        if board.is_terminal_state(self.symbol, self.oppSym):
            if self.utility(board) > 0:
                print('Max Win')
                return self.utility(board) + 5000, None
            if self.utility(board) < 0:
                print('Max Loss')
                return self.utility(board) - 5000, None
        if depth == 0:
            return self.utility(board), None
        else:
            v, move = float('-inf'), None
            moves = self.successor(board)
            if moves == []:
                temp_board = board.clone_of_board()
                v2, a2 = self.max_value(temp_board, depth - 1)
                if v2 > v:
                    v, move = v2, None
                return v, move
            for a in moves:
                succ_board = board.clone_of_board()
                col = a[0]
                row = a[1]
                succ_board.play_move(col, row, self.symbol)
                opp = MinimaxPlayer(self.oppSym)
                v2, a2 = opp.min_value(succ_board, depth-1)
                if v2 > v:
                    v, move = v2, a
            return v, move
            # function MAX-VALUE(game, state) returns a(utility, move) pair
            #     if game.IS-TERMINAL(state) then return game.UTILITY (state, player), null
            #     v, move <- -∞, null
            #     for each a in game.ACTIONS(state) do
            #     v2, a2 <- MIN-VALUE(game, game.RESULT(state, a)) 
            #     if v2 > v then
            #         v, move <- v2, a
            #     return v, move

# function MIN-VALUE(game, state) returns a(utility, move) pair
    # if game.IS-TERMINAL(state) then return game.UTILITY (state, player), null
    # v, move <- +∞, null
    # for each a in game.ACTIONS(state) do
    # v2, a2 <- MAX-VALUE(game, game.RESULT(state, a)) 
    #if v2 < v then
        # v, move <- v2, a 
    #return v, move
    def min_value(self, board, depth):
        if board.is_terminal_state(self.symbol, self.oppSym):
            if self.utility(board) > 0:
                return self.utility(board) + 5000, None
            if self.utility(board) < 0:
                return self.utility(board) - 5000, None
        if depth == 0:
            return self.utility(board), None
        else:
            v, move = float('inf'), None
            moves = self.successor(board)
            if moves == []:
                temp_board = board.clone_of_board()
                v2, a2 = self.min_value(temp_board, depth -1)
                if v2 < v:
                    v, move = v2, None
                return v, move
            for a in moves:
                succ_board = board.clone_of_board()
                col = a[0]
                row = a[1]
                succ_board.play_move(col, row, self.oppSym)
                opp = MinimaxPlayer(self.oppSym)
                v2, a2 = opp.max_value(succ_board, depth-1)
                if v2 < v:
                    v, move = v2, a
            return v, move

    def get_move(self, board):
        self.time_start = time.time()
        result = self.minimax_search(board, 16)
        # print("result: ", result)
        col = result[0]
        row = result[1]
        self.time_end = time.time()
        print("Time taken:", self.time_end - self.time_start, "seconds")
        self.total_time += (self.time_end - self.time_start)
        print( "total time :", self.total_time)
        self.num_moves += 1
        print ("total moves =", self.num_moves)
        return col, row

#         #- You will need to implement the Minimax-Decision, Max-Value and Min-Value functions on that slide. You should be sure to include a depth parameter to ensure that your minimax player will make a decision in a timely manner (less than two seconds), regardless of the board size. You will need to come up with a heuristic evaluation function to apply when you hit the depth limit in your search. You will need to override the default get_move function of the Player class for the MinimaxPlayer class in order to produce an action using Minimax.
#         # In addition to the functionality described above, you may need to implement some other code to
#         # do things like bookkeeping.