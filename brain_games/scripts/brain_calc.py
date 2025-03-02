import random

from brain_games.game_engine import play_game

def calc_game_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"

    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return question, str(answer)

def main():
    play_game(calc_game_logic)

if __name__ == "__main__":
    main()

