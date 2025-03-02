import random

from brain_games.game_engine import play_game

def main():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"

    print("What is the result of the expression?")

    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return question, answer

if __name__ == "__main__":
    play_game(main)

