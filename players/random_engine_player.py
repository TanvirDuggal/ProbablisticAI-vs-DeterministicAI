import random
import chess
from players.base_player import BasePlayer


class RandomEnginePlayer(BasePlayer):
    def __init__(self, name: str = "RandomEngine"):
        super().__init__(name)

    def get_move(self, board: chess.Board) -> chess.Move:
        legal_moves = list(board.legal_moves)
        return random.choice(legal_moves)