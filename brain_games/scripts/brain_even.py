import random
import game_engine

def is_even_game_logic():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer

def main():
    play_game(is_even_game_logic)

if __name__ == "__main__":
    main()

