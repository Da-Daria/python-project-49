import random

def even_game_logic():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer

if __name__ == "__main__":
    play_game(even_game_logic)

