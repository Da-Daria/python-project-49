import random




def get_question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"


    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
 
    return question, answer





def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    

    for _ in range(3):
        question, correct_answer = get_question_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        
        if int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. 
            Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
