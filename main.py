from game_functions import *
import time

# Loop to handle the initial choice of whether the user wants to play or see the instructions.
while True:
    user_choice = get_user_choice()
    if user_choice == "play":
        print("Let's start the game! 🚀")
        break
    elif user_choice == "info":
        print("Here's how you play the game... ")
        show_info()
    else:
        print("Invalid choice. Please try again. ❌")

# This loop ensures the user inputs a valid number of problems they want to solve.
on = True
while on:    
    try:
        total_problems = int(input("\nChoose number of problems: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    while True:
        level = input("Level (Easy - Medium - Hard - Insane) : ").strip().lower()
        if level in LEVELS:
            operators = LEVELS[level]["operators"]
            min_operand = LEVELS[level]["min_operand"]
            max_operand = LEVELS[level]["max_operand"]
            break
        else:
            print("Invalid input! Please choose between levels: Easy, Medium, Hard, or Insane.")



    wrong = 0
    correct = 0


    input("Press Enter to start!")
    print("------------------------------------------")

    # After setting up the number of problems and difficulty, the game starts.
    start_time = time.time()
    # Loop to present each problem and prompt the user for an answer.
    for i in range(total_problems):
        expr, answer = generate_a_problem(min_operand, max_operand, operators)
        while True:
            guess = int(input(f"Problem {i + 1} :\t{expr} = "))
            if guess == answer:
                correct += 1
                break
            else:
                wrong += 1
                break

    end_time = time.time()
    total_time = end_time - start_time
    # After the game ends, the total time taken and the user's score (correct and wrong answers) are displayed.
    print("------------------------------------------")
    print(f"🎉 Great Job! 🎉\nCorrect: {correct}\nWrong: {wrong}\nAccuracy: {(correct/total_problems)*100:.2f}%\nTime Taken: {total_time:.2f} seconds")
    print("------------------------------------------")
    on = True if input("Would you like to play again ? (y/n): ").lower() == "y" else False

print("Game Closed !")
time.sleep(10)