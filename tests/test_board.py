import pytest
import chess
from blind_fischer_chess import BFChess

class TestBoard():
    def setup_method(self):
        self.game = BFChess()
    def test_set_start_position(self):
        ## this should pass
        game = self.game
        game.set_start_position('rnbqkbnr', chess.WHITE)
        game.set_start_position('Rnbqkbnr', chess.BLACK)
        game.set_start_position('rbknbnqr', chess.WHITE)

        ## other piece types not allowed
        with pytest.raises(ValueError):
            game.set_start_position('rbbkanqr', chess.WHITE)

        ## two queens not allowed
        with pytest.raises(ValueError):
            game.set_start_position('rbkanqqr', chess.WHITE)
            
        ## more than eight pieces not allowed
        with pytest.raises(ValueError):
            game.set_start_position('rbbknnnqr', chess.WHITE)

        ## both bischoffs cannot be on black field
        with pytest.raises(ValueError):
            game.set_start_position('rbkbnnqr', chess.WHITE)

        ## king has to be between the rooks
        with pytest.raises(ValueError):
            game.set_start_position('bkrbnnqr', chess.WHITE)
