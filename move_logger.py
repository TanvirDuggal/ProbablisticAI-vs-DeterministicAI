class MoveLogger:
    def __init__(self, file_path: str = "moves.txt"):
        self.file_path = file_path

        # Clear file at the start of a new game
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write("Game Moves\n")
            file.write("==========\n")

    def log_move(self, move_number: int, player_name: str, move_uci: str) -> None:
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(f"{move_number}. {player_name}: {move_uci}\n")

    def log_result(self, result: str, winner: str | None):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write("\n==========\n")
            file.write(f"Result: {result}\n")

            if winner:
                file.write(f"Winner: {winner}\n")
            else:
                file.write("Game drawn\n")

            file.write("\n+++++++++++++++++++++++++\n")