import math
import random

from brain_games.game_engine import play_game


def gcd(a, b):
    return math.gcd(a, b)


def gcd_game_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = gcd(num1, num2)
    return question, str(correct_answer)


def main():
    print("Find the greatest common divisor of given numbers.")
    play_game(gcd_game_logic)


if __name__ == "__main__":
    main()

