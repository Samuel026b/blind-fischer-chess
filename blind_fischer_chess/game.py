import chess

class BFChess():
    def __init__(self):
        self.board = None
    def set_start_position(self, position, player):
        ## This method can only be used before the game has started.
        if self.board:
            raise ValueError("start position can only be set before the game has started")
        
        ## Verify the position
        position = position.lower()
        if sorted(position) != ['b', 'b', 'k', 'n', 'n', 'q', 'r', 'r']:
            raise ValueError("Invalid start position - need a string like 'rnbqkbnr'")

        ## bishops should be on white and black fields
        b1 = position.find('b')
        b2 = position.find('b', b1+1)
        if b1%2 + b2%2 != 1:
            raise ValueError("bishops should be on white and black fields")

        ## king must be between the rooks
        r1 = position.find('r')
        r2 = position.find('r', r1+1)
        k = position.find('k')
        if r1 > k or r2 < k:
            raise ValueError("king must be between the rooks")

        ## Upper case for white, lower case for black
        if player == chess.WHITE:
            self.white_start_position = position.upper()
        elif player == chess.BLACK:
            self.black_start_position = position.lower()
        else:
            raise ValueError("invalid player")
        
