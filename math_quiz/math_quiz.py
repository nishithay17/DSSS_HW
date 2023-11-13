import random

# function to select a random integer
def random_int(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

# function to select a random mathematical operator
def random_choice():
    return random.choice(['+', '-', '*'])

# mathematical operator execution function
def fun_operator(num1, num2, op):
    prob = f"{num1} {op} {num2}"
    if op == '+': result = num1 + num2
    elif op == '-': result = num1 - num2
    else: result = num1 * num2
    return prob, result

def math_quiz():
    initial_points = 0
    no_questions = 6

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(no_questions):
        num1 = random_int(1, 15); num2 = random_int(1, 10); op = random_choice()

        PROBLEM, ANSWER = fun_operator(num1, num2, op)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer:  ")
        try:
            useranswer = int(useranswer)
        except:
            print("Please enter a valid input")
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            initial_points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {initial_points}/{no_questions}")

if __name__ == "__main__":
    math_quiz()
