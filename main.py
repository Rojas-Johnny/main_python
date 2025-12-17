import random

def math_game():
    print("\nMath Multiplication Game:")
    print("Choose your difficulty: 1 (Easy), 2 (Medium), 3 (Hard)")
    score = 0
    
    while True:
        user_choice = input("Select level 1, 2, or 3: ").strip()
        if user_choice == "1":
            max_num = 10
            mode = "Easy"
            break
        elif user_choice == "2":
            max_num = 20
            mode = "Medium"
            break
        elif user_choice == "3":
            max_num = 30
            mode = "Hard"
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    print(f"\nYou selected {mode} mode. Type q to quit.")
    
    while True:
        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)
        correct_answer = num1 * num2

        user_input = input(f"\nWhat is {num1} * {num2}? ").lower().strip()
        if user_input == 'q':
            print(f"\nFinal Score: {score}")
            break
        try:
            input1 = int(user_input)
            if input1 == correct_answer:
                print("\nCorrect!")
                score += 1
            else:
                print(f"\nWrong! The correct answer is {correct_answer}")
                score -= 1
        except ValueError:
            print("\nPlease type a number or q to quit")

math_game()