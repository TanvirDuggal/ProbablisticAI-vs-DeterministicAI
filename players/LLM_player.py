import json
import random
import chess
from openai import OpenAI
from players.base_player import BasePlayer


class LLMPlayer(BasePlayer):
    def __init__(
        self,
        name: str = "Grandmaster-LLM",
        model: str = "gpt-5.4-mini",
    ):
        super().__init__(name)

        # 🔑 Hardcoded API key (for local testing only)
        self.client = OpenAI(
            api_key=""
        )

        self.model = model

    def get_move(self, board: chess.Board) -> chess.Move:
        legal_moves = [move.uci() for move in board.legal_moves]
        previous_moves = [move.uci() for move in board.move_stack]

        prompt = self._build_prompt(board, legal_moves, previous_moves)

        try:
            response = self.client.responses.create(
                model=self.model,
                input=prompt,
                text={
                    "format": {
                        "type": "json_schema",
                        "name": "chess_move",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "move": {"type": "string"},
                                "reason": {"type": "string"}
                            },
                            "required": ["move", "reason"],
                            "additionalProperties": False
                        },
                        "strict": True
                    }
                }
            )

            data = json.loads(response.output_text)
            move_uci = data["move"]

            if move_uci not in legal_moves:
                print("⚠️ Invalid move from LLM, using fallback")
                move_uci = random.choice(legal_moves)

        except Exception as e:
            print(f"⚠️ LLM failed: {e}")
            move_uci = random.choice(legal_moves)

        return chess.Move.from_uci(move_uci)

    def _build_prompt(self, board, legal_moves, previous_moves):
        moves_text = ", ".join(previous_moves) if previous_moves else "No moves yet"

        return f"""
        You are a GRANDMASTER-level chess player.

        Your task is to choose the strongest legal move from the provided legal_moves list.

        Analyze the position internally using these priorities:
        1. King safety
        2. Checks, captures, and immediate tactics
        3. Opponent threats
        4. Piece development and activity
        5. Control of the center
        6. Pawn structure
        7. Long-term positional advantage

        Use the previous moves and current board position to understand the game context.

        STRICT RULES:
        - Choose exactly one move from legal_moves.
        - Do not invent a move.
        - Do not return an illegal move.
        - Return ONLY valid JSON.
        - Do not include markdown.
        - Do not include extra text outside JSON.
        - Keep the reason short.

        FEN:
        {board.fen()}

        Previous moves:
        {moves_text}

        Legal moves:
        {legal_moves}

        Return:
        {{
        "move": "<one move from legal_moves>",
        "reason": "<short explanation>"
        }}
        """.strip()

    def close(self):
        pass