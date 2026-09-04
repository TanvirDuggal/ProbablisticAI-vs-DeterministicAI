from abc import ABC, abstractmethod
import chess


class BasePlayer(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_move(self, board: chess.Board) -> chess.Move:
        pass

    def close(self) -> None:
        pass