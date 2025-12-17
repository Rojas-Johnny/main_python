import random
def math_game():
    print("\nMath Multiplcation Game:")
    score = 0

    while True:
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        correct_answer = num1 * num2

        user_input = input(f"\nWhat is {num1} * {num2}? ").lower().strip()
        if user_input =='q':
            print(f"\nFinal Score: {score}")
            break
        if not user_input.isdigit():
            print("\nEnter a number: ")
        if int(user_input) == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}")
            score =- 1
math_game()