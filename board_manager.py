import chess


class BoardManager:
    def __init__(self):
        self.board = chess.Board()

    def get_board(self) -> chess.Board:
        return self.board

    def apply_move(self, move: chess.Move) -> None:
        self.board.push(move)

    def is_game_over(self) -> bool:
        return self.board.is_game_over()

    def result(self) -> str:
        return self.board.result()

    def print_board(self) -> None:
        print("\n" + str(self.board))
        print("\nFEN:", self.board.fen())

    def print_status(self) -> None:
        if self.board.is_check():
            print("Check!")

    def print_game_result(self) -> None:
        print("\nGame Over")
        print("Result:", self.board.result())

        if self.board.is_checkmate():
            winner = "Black" if self.board.turn == chess.WHITE else "White"
            print(f"Checkmate. {winner} wins.")
        elif self.board.is_stalemate():
            print("Draw by stalemate.")
        elif self.board.is_insufficient_material():
            print("Draw by insufficient material.")
        elif self.board.is_fivefold_repetition():
            print("Draw by repetition.")
        elif self.board.is_seventyfive_moves():
            print("Draw by 75-move rule.")