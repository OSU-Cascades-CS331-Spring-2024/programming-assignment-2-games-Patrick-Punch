'''
    Defines Player class, and subclasses Human and Minimax Player.
'''

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
        # print('Infinity', float('inf'))
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
        #     Source: http://home.datacomm.ch/t_wolf/tw/misc/reversi/html/index.html
        #     - Mobility
        #         A better criterion for determining a position is to count the number of moves a player can make: the mobility is decisive in Reversi! If you only have a few moves, it's likely that your opponent can play such that you are forced to make bad moves. Therefore, if your mobility is high, the position is better for you than if it's low.
        #     - Potential mobility
        #         Potential mobility can be estimated by simply counting all the opponent's pieces that are adjacent to an empty field.
        #     - Edge table
        #         This table is precomputed by starting with all possible positions and then playing a one-dimensional Reversi game (allowing passes at any move) to the end. The resulting percentage of victories for a given starting position determines that edge configuration's value.
        #     - Corner ratio
        #         sometimes it would play onto a square diagonally adjacent to a corner when this subsequently made it lose that corner. To cure that, I biased the priority table (see above) against such moves. In addition, I also incorporated the number of occupied corners in the evaluation function. Generally (though there are exceptions!!), it is good to move to a corner. The program therefore calculates part of the evaluation function from the ratio of the numbers of corners owned by itself and its opponent.

    def successor(self, board):
        result = []
        scores = []
        available_moves = board.num_legal_moves_remaining(self.symbol)
        # print(len(available_moves),"Available Moves: ", available_moves)
        # for move in available_moves:
        #     # opp = MinimaxPlayer(self.oppSym)
        #     succ_board = board.clone_of_board()
        #     col = move[0]
        #     row = move[1]
        #     succ_board.play_move(col, row, self.symbol)
        #     score = succ_board.count_score(self.symbol)
        #     if move == [0,0] or move == [3,3] or move == [0,3] or move == [3,0]:
        #         score += 5
        #         # print("Test Weighted Corner Score: ", score)
        #     scores.append([score, move])
        #     # print("\nBoard after Selecting Move: ", move, "Score: ", score)
        #     # succ_board.display()
        #     result.append(succ_board)
        # # print(result)
        # # print(scores)
        # print("Reccomended Move: ", max(scores))
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

    def is_cornered(self, board, symbol):
        weighted_score = 0
        corners = [[0,0], [0, 3], [3,0], [3,3]]
        for pos in corners:
            c = pos[0]
            r = pos[1]
            if board.grid[c][r] == symbol:
                weighted_score += 5
        return weighted_score

#function MAX-VALUE(game, state) returns a(utility, move) pair
    # if game.IS-TERMINAL(state) then return game.UTILITY (state, player), null
    # v, move <- -∞, null
    # for each a in game.ACTIONS(state) do
    # v2, a2 <- MIN-VALUE(game, game.RESULT(state, a)) 
    # if v2 > v then
        # v, move <- v2, a
    # return v, move
    def max_value(self, board, depth):
        if board.is_terminal_state(self.symbol, self.oppSym):
            if self.utility(board) == 1:
                print('Max Win')
                return self.utility(board) + self.is_cornered(board, self.symbol) + 5, None
            if self.utility(board) == 0:
                print('Max Tie')
                return self.utility(board) + self.is_cornered(board, self.symbol) + 1, None
            if self.utility(board) == -1:
                print('Max Loss')
                return self.utility(board) - self.is_cornered(board, self.symbol) - 5, None
        if depth == 0:
            # print('Max Outcome State: ', self.utility(board))
            return self.utility(board) + self.is_cornered(board, self.symbol), None
        else:
            v, move = float('-inf'), None
            moves = self.successor(board)
            if moves == []:
                print('Skipping (max) turn')
                temp_board = board.clone_of_board()
                v2, a2 = self.min_value(temp_board, depth -1)
                if v2 > v:
                    v, move = v2, None
                return v, move
            # print("MAX (O) moves: ", self.symbol, moves)
            for a in moves:
                # print("MAX Move ->", a)
                succ_board = board.clone_of_board()
                col = a[0]
                row = a[1]
                succ_board.play_move(col, row, self.symbol)
                # print("\nMAX --")
                # succ_board.display()
                v2, a2 = self.min_value(succ_board, depth-1)
                # print("Max - V2, A2: ", v2, a2, "V, A: ", v, a)
                if v2 > v:
                    v, move = v2, a
                # print("MAX V,move,v2,a2 ->", v, move, v2, a2)
                # else:
                    # print("symbol score -> ", board.count_score(self.symbol), "move -> ", a, "v -> ", v, "default move", move, 'v2 -> ', v2, 'a2 -> ', a2)
            # print('foo-max')
            if move is None:
                print("look here dummy ", moves)
            return v, move

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
            if self.utility(board) == 1:
                print("Min Win")
                return self.utility(board) + self.is_cornered(board, self.symbol) + 5, None
            if self.utility(board) == 0:
                print('Min Tie')
                return self.utility(board) + self.is_cornered(board, self.symbol) + 1, None
            if self.utility(board) == -1:
                print('Min Loss')
                return self.utility(board) - self.is_cornered(board, self.symbol) - 5, None
        if depth == 0:
            # print('Mini Outcome State: ', self.utility(board))
            # # board.display()
            # # print('mini solution ^^^^')
            return self.utility(board) + self.is_cornered(board, self.symbol), None
        else:
            v, move = float('inf'), None
            moves = self.successor(board)
            if moves == []:
                print('Skipping (min) turn')
                temp_board = board.clone_of_board()
                v2, a2 = self.max_value(temp_board, depth -1)
                if v2 < v:
                    v, move = v2, None
                return v, move
            # print("Min (X) moves ->", self.oppSym, moves)
            for a in moves:
                # print('mini move -> ', a)
                succ_board = board.clone_of_board()
                # print('Column,Row of Move: ', a, 'c: ', a[0], 'r: ', a[1])
                col = a[0]
                row = a[1]
                succ_board.play_move(col, row, self.oppSym)
                # print('\n mini --')
                # succ_board.display()
                v2, a2 = self.max_value(succ_board, depth-1)
                # print("Min - V2, A2: ", v2, a2, "V, A: ", v, a)
                if v2 < v:
                    v, move = v2, a
            return v, move

    def get_move(self, board):
        result = self.minimax_search(board, 16)
        print(result)
        col = result[0]
        row = result[1]
        return col, row
    
        #- You will need to implement the Minimax-Decision, Max-Value and Min-Value functions on that slide. You should be sure to include a depth parameter to ensure that your minimax player will make a decision in a timely manner (less than two seconds), regardless of the board size. You will need to come up with a heuristic evaluation function to apply when you hit the depth limit in your search. You will need to override the default get_move function of the Player class for the MinimaxPlayer class in order to produce an action using Minimax.
        # In addition to the functionality described above, you may need to implement some other code to
        # do things like bookkeeping.


# wikipedia pseudocode: -https://en.wikipedia.org/wiki/Minimax
# function minimax(node, depth, maximizingPlayer) is
#     if depth = 0 or node is a terminal node then
#         return the heuristic value of node
#     if maximizingPlayer then
#         value := −∞
#         for each child of node do
#             value := max(value, minimax(child, depth − 1, FALSE))
#         return value
#     else (* minimizing player *)
#         value := +∞
#         for each child of node do
#             value := min(value, minimax(child, depth − 1, TRUE))
#         return value






