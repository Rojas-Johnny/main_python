import random
def math_game():
    print("\nMath Multiplcation Game:")
    score = 0

    while True:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        correct_answer = num1 * num2

        user_input = input(f"\nWhat is {num1} * {num2}? ").lower().strip()
        if user_input =='q':
            print(f"\nFinal Score: {score}")
            break
        try:
            input1 = int(user_input)
            
            if input1 == correct_answer:
                print("\nCorrect!")
                score += 1
            else:
                print (f"\nWrong! The correct answer is {correct_answer}")
                score -= 1
        except ValueError:
            print("\nPlease type a number or q to quit")
math_game()