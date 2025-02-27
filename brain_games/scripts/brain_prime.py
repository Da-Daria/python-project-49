import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def game_logic():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer

def main():
    play_game(game_logic)

if __name__ == "__main__":
    main()

