import random
from brain_games.cli import welcome_user

def is_even(num):
    return num % 2 == 0

def brain_even():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = input('Your answer: ').strip().lower()

        correct_answer = 'yes' if is_even(number) else 'no'

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again!")
            return

    print(f'Congratulations!')

if __name__ == '__main__':
    brain_even()
