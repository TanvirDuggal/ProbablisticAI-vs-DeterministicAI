import chess
from players.base_player import BasePlayer


class HumanPlayer(BasePlayer):
    def __init__(self, name: str = "Human"):
        super().__init__(name)

    def get_move(self, board: chess.Board) -> chess.Move:
        while True:
            user_input = input("Enter your move in UCI format (e.g. e2e4): ").strip().lower()

            if user_input == "quit":
                raise SystemExit("Game ended by user.")

            try:
                move = chess.Move.from_uci(user_input)
            except ValueError:
                print("Invalid move format. Try again.")
                continue

            if move not in board.legal_moves:
                print("Illegal move. Try again.")
                continue

            return move