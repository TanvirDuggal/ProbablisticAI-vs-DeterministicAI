import chess
from board_manager import BoardManager
from players.base_player import BasePlayer
from move_logger import MoveLogger


class GameRunner:
    def __init__(self, white_player: BasePlayer, black_player: BasePlayer):
        self.white_player = white_player
        self.black_player = black_player
        self.board_manager = BoardManager()
        self.move_logger = MoveLogger("moves.txt")

    def run(self) -> None:
        board = self.board_manager.get_board()

        try:
            while not self.board_manager.is_game_over():
                self.board_manager.print_board()

                current_player = (
                    self.white_player if board.turn == chess.WHITE else self.black_player
                )

                print(f"\nTurn: {current_player.name}")
                move = current_player.get_move(board)

                print(f"{current_player.name} plays: {move}")
                self.board_manager.apply_move(move)

                move_number = board.fullmove_number
                if board.turn == chess.WHITE:
                    # This means black just moved, so the visible move number is one less
                    move_number -= 1

                self.move_logger.log_move(
                    move_number=move_number,
                    player_name=current_player.name,
                    move_uci=str(move),
                )

                self.board_manager.print_status()

            result = board.result()
            winner = None
            if board.is_checkmate():
                winner = (
                    self.black_player.name
                    if board.turn == chess.WHITE
                    else self.white_player.name
                )

            self.move_logger.log_result(result=result, winner=winner)

            self.board_manager.print_board()
            self.board_manager.print_game_result()

        finally:
            self.white_player.close()
            self.black_player.close()