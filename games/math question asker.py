import random

def generate_math_problem():
    """Generate a random math problem."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    problem = f"{num1} {operator} {num2}"
    return problem

def main():
    print("Welcome to the Math Quiz!")
    score = 0
    num_questions = 5  # You can adjust the number of questions

    for _ in range(num_questions):
        math_problem = generate_math_problem()
        user_answer = input(f"What is the answer to {math_problem}? ")

        try:
            correct_answer = eval(math_problem)
            user_answer = int(user_answer)

            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}\n")
        except:
            print("Invalid input. Please enter a valid number.\n")

    print(f"You scored {score}/{num_questions}. Thanks for playing!")

if __name__ == "__main__":
    main()
