# This code was created by Kevin Walsh, and used for comparing time complexity with my own implementation

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
        self.time_start=0
        self.time_end=0
        self.total_time = 0 
        self.total_moves= 0 
  
        

        
        # self.all_boards={}
    def Utility(self, board):
        return (board.count_score('X')-board.count_score('O'))
    
    def get_move(self, board):
        self.time_start = time.time()

        if self.symbol=='X':

            x = self.symbol
        else :
            x = 'O'
        
        move , value= self.minimax( board, -1, x )
        self.end_time = time.time()
        print("Time taken:", self.end_time - self.time_start, "seconds")
        self.total_time+= (self.end_time-self.time_start)
        print( "total time :", self.total_time)
        self.total_moves+=1
        print ("total moves =", self.total_moves)
        return move


    def Successor(self, board , symbol):

        
        legal_moves = board.total_legal_moves_remaining(symbol)
        
        return legal_moves

    

        
    def minimax(self, board,depth, symbol):
        if symbol == 'X':
            
            oppSym = 'O'
        else:
            oppSym= 'X'

        if  (depth == 0 ):
            return None, self.Utility(board)
        
        if (not board.has_legal_moves_remaining( symbol) ):
            if self.Utility(board)<0:
                return None ,float('-inf') 
            else:
                return None , float('inf')
            

        

        if symbol == 'X':
            best_value =  float('-inf')
            legal_moves = self.Successor(board , symbol)
            for move in legal_moves:

                new_board= board.clone_of_board()

                new_board.play_move(move[0],move[1],symbol)
                
                next_move, value = self.minimax(new_board, depth-1 ,oppSym) 
                
                best_value = max(best_value, value)

                if value == best_value:
                    best_move = move
            return best_move, best_value
        else:
            best_value =float('inf') 
            legal_moves = self.Successor(board,symbol) 
            for move in legal_moves:

                new_board= board.clone_of_board()

                new_board.play_move(move[0],move[1],symbol)
                next_move, value = self.minimax(new_board, depth-1, oppSym ) 
                
                best_value = min(best_value, value)

                if value == best_value:
                    best_move = move

            return best_move, best_value
            
    def __min__(input1, input2):
        if input1 > input2:
            return input2
        else:
            return input1

    def __max__(input1, input2):
        if input1 < input2:
            return input2
        else:
            return input1
