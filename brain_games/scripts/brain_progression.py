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

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    for _ in range(3):
        progression = generate_progression()
        hidden_value, displayed_progression = hide_element(progression)

        print("Question:", ' '.join(map(str, displayed_progression)))
        user_answer = input("Your answer: ")

        if int(user_answer) == hidden_value:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_value}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
