import random
from brain_games.game_engine import play_game

def generate_progression(start, step, length):
    return [start + step * i for i in range(length)]

def progression_game_logic():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    length = 10

    progression = generate_progression(start, step, length)
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))
    return question, str(correct_answer)

def main():
    print("What number is missing in the progression?")
    play_game(progression_game_logic)

if __name__ == "__main__":
    main()
