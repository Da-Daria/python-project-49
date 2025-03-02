import math
import random

from game_engine import play_game


def gcd_game_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = math.gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, correct_answer


if __name__ == "__main__":
    play_game(gcd_game_logic)
