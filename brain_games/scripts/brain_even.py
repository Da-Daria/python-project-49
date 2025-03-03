import random

from brain_games.game_engine import play_game


def is_even_game_logic():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play_game(is_even_game_logic)


if __name__ == "__main__":
    main()

