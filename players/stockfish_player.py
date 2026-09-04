import chess
import chess.engine
from players.base_player import BasePlayer


class StockfishPlayer(BasePlayer):
    def __init__(
        self,
        engine_path: str,
        name: str = "Stockfish",
        move_time: float = 0.3,
        skill_level: int | None = None,
    ):
        super().__init__(name)
        self.engine = chess.engine.SimpleEngine.popen_uci(engine_path)
        self.move_time = move_time

        if skill_level is not None:
            self.engine.configure({"Skill Level": skill_level})

    def get_move(self, board: chess.Board) -> chess.Move:
        result = self.engine.play(board, chess.engine.Limit(time=self.move_time))
        return result.move

    def close(self) -> None:
        self.engine.quit()