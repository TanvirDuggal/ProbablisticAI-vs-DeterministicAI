from game_runner import GameRunner
from players.human_player import HumanPlayer
from players.stockfish_player import StockfishPlayer
from players.random_engine_player import RandomEnginePlayer
from players.LLM_player import LLMPlayer


STOCKFISH_PATH = r""


def build_engine(choice: str):
    if choice == "1":
        return StockfishPlayer(
            engine_path=STOCKFISH_PATH,
            name="Stockfish",
            move_time=0.3,
            skill_level=5,
        )
    if choice == "2":
        return LLMPlayer(
            name="OpenAI-LLM",
            model="gpt-5.4-mini",
        )
    raise ValueError("Invalid engine choice")


def main():
    print("Current players")
    print("1. Stockfish - White")
    print("2. OpenAI LLM - Black")

    for _ in range(300):
        white_player = build_engine("2")
        black_player = build_engine("1")
        game = GameRunner(white_player, black_player)
        game.run()


if __name__ == "__main__":
    main()