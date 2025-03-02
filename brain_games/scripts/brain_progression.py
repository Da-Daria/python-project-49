import random


def generate_progression(length=None, start=1, step=2):
    if length is None:
        length = random.randint(5, 10)
    return [start + step * i for i in range(length)]


def hide_element(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return hidden_value, progression


def game_logic():
    progression = generate_progression()
    hidden_value, displayed_progression = hide_element(progression)
    question = ' '.join(map(str, displayed_progression))
    return question, hidden_value


if __name__ == "__main__":
    play_game(game_logic)

