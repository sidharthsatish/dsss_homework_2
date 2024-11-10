import random

def generate_random_integer(min_val, max_val):
    """Returns a random integer between min_val and max_val (inclusive)."""
    return random.randint(min_val, max_val)

def choose_operator():
    """Randomly selects an operator from '+', '-', and '*'."""
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """
    Creates a math problem and computes an intentionally incorrect answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        incorrect_answer = num1 - num2
    elif operator == '-':
        incorrect_answer = num1 + num2
    else:  # operator == '*'
        incorrect_answer = num1 * num2
    return problem, incorrect_answer

def math_quiz():
    """Runs a Math Quiz Game with randomly generated questions."""
    score = 0
    total_questions = 3  # Number of quiz questions

    print("Welcome to the Math Quiz Game!")
    print("Answer the questions correctly to earn points.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = choose_operator()

        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
