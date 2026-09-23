# Stockfish vs LLM Chess Gameplay Framework

# PDF Link : https://www.academia.edu/176084511/Deterministic_AI_vs_Probabilistic_AI_Comparing_Stockfish_and_LLM_Based_Chess_Gameplay

This project implements an automated chess gameplay framework for comparing a deterministic search-based chess engine, Stockfish, with an LLM-based probabilistic chess agent using ChatGPT. The system allows both agents to play chess against each other under controlled configurations while logging moves and final game outcomes for post-game analysis.

The main objective of this project is to study the difference between traditional chess-engine decision-making and LLM-based move generation. Stockfish selects moves through deterministic search, pruning, and board evaluation, while the LLM-based agent generates moves using previous move history, legal move information, and prompt-based reasoning.

## Project Overview

The framework is built in Python and uses the `python-chess` library to manage board state, legal move validation, turn execution, and game termination conditions. Stockfish is integrated locally as the deterministic chess engine, while the LLM-based agent is connected through the OpenAI API.

The system supports repeated automated gameplay, where each completed game is logged for later analysis. The logs include move number, player identity, moves made by each agent, and the final result of the game.

## Features

* Automated chess gameplay between Stockfish and a ChatGPT-based LLM agent
* Support for both color configurations:

  * Stockfish as White and LLM as Black
  * LLM as White and Stockfish as Black
* Legal move validation using `python-chess`
* Local Stockfish engine integration
* OpenAI API integration for LLM-based move generation
* Move history provided as contextual input to the LLM
* Text-based move logging for post-game analysis
* Support for repeated game execution

## System Architecture

The framework follows a modular structure where each component handles a specific responsibility:

* **Board Manager**: Maintains the chess board state, validates moves, and checks game termination conditions.
* **Stockfish Player**: Connects to the locally installed Stockfish engine and generates deterministic chess moves.
* **LLM Player**: Uses the OpenAI API to generate moves based on previous move history and legal move constraints.
* **Game Runner**: Coordinates turn execution between both players until the game ends.
* **Move Logger**: Records gameplay data in a local text file for analysis.

## Gameplay Flow

Each game begins by initializing a chess board and assigning White and Black roles to the two agents. The White player makes the first move, after which the move is validated and applied to the board. The move is then logged, and the turn switches to the opposing player.

For the LLM-based agent, previous move history is included in the prompt as contextual input. The model is instructed to generate a legal chess move based on the current gameplay sequence. If an invalid move is generated, the system can reject it and request another move depending on the implementation.

The game continues until a termination condition such as checkmate, stalemate, draw, or another game-ending state is reached.

## Experimental Purpose

This project was created to support a comparative study between deterministic AI and probabilistic AI in chess gameplay.

The experiment evaluates whether a raw general-purpose LLM can compete against a specialized chess engine when both are placed in the same gameplay environment. The LLM-based agent is not fine-tuned on chess, does not use external search, and does not receive engine-assisted move evaluation. Its decisions are based on prompt context, previous move history, and learned chess-related patterns.

## Technologies Used

* Python
* python-chess
* Stockfish chess engine
* OpenAI API
* Text-based logging

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not available, install the main dependency manually:

```bash
pip install chess openai
```

### 3. Download Stockfish

Download Stockfish from the official website:

```text
https://stockfishchess.org/download/
```

After downloading, update the Stockfish executable path in the project configuration or source code.

Example:

```python
STOCKFISH_PATH = "path/to/stockfish"
```

### 4. Configure OpenAI API Key

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key"
```

For Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your-api-key"
```

### 5. Run the Project

```bash
python main.py
```

The exact command may vary depending on your project structure.

## Output

The system generates a text-based move log containing gameplay information such as:

* Game number
* Move number
* Player name
* Move played
* Final game result

Example:

```text
Game 1
Move 1: Stockfish played e2e4
Move 1: LLM played e7e5
...
Result: Stockfish wins
```

These logs can be used for statistical analysis, including win rate, game length distribution, opening move behavior, capture activity, and piece movement patterns.

## Research Context

This project supports analysis of the difference between chess-like move generation and competitive chess performance. The LLM-based agent may generate recognizable opening moves such as `e2e4`, `e7e5`, `d7d5`, or `g8f6`, but it does not explicitly search future game states or evaluate resulting board positions like Stockfish.

The project therefore highlights the limitations of raw LLM-based gameplay in adversarial environments that require tactical verification, material preservation, king safety, and long-term strategic planning.

## Limitations

* The LLM agent is evaluated in a raw, unassisted state.
* The LLM is not fine-tuned on chess-specific datasets.
* The LLM does not use external search or Stockfish-based move evaluation.
* The experiment compares two fundamentally different decision-making mechanisms.
* Move quality is primarily analyzed through logs and outcomes rather than full engine evaluation of every position.

## Future Work

Future improvements may include:

* Testing multiple LLM models
* Using structured board-state representation such as FEN
* Fine-tuning an LLM on chess game data
* Adding engine-based evaluation after each move
* Comparing different prompting strategies
* Building a hybrid system combining LLM reasoning with Stockfish evaluation
* Visualizing move-by-move evaluation scores

## Disclaimer

This project does not claim that LLMs cannot be improved for chess. The experiment evaluates a raw general-purpose LLM as a standalone chess-playing agent. Prior research suggests that LLM chess performance can improve through supervised fine-tuning, structured board-state representation, and chess-specific configuration.

## License

This project is intended for educational and research purposes. Add a license file if you plan to make the repository publicly reusable.
