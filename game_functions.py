import os
import random

# Ultimate Math Challenge Game
# This game presents users with random math problems based on the selected difficulty level.
# The user can choose from four levels: Easy, Medium, Hard, and Insane, each with different operators and operand ranges.
# The goal is to answer as many questions correctly and as quickly as possible.

# Dictionary to store the difficulty levels and their corresponding parameters
LEVELS = {
    "insane": {"operators": ["+", "-", "*"], "min_operand": 100, "max_operand": 500},
    "hard": {"operators": ["+", "-", "*"], "min_operand": 10, "max_operand": 50},
    "medium": {"operators": ["+", "-"], "min_operand": 10, "max_operand": 30},
    "easy": {"operators": ["+"], "min_operand": 0, "max_operand": 20},
    }


# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to generate a random math problem based on difficulty level
def generate_a_problem(min_operand, max_operand, operators):
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operators)
    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer


# Function to display the main menu and get the user's choice
def get_user_choice():
    """Displays a welcome message and gets the user's choice."""
    choice = input(
        "🎮 Welcome to the Ultimate Math Challenge! 🎉\n\n"
        "🟢 Ready to test your skills?\n"
        "👉 Type 'play' to start playing!\n"
        "Or type 'info' to learn how the game works.\n\n"
        "Your choice: "
    ).strip().lower()
    return choice


# Function to display the game instructions and rules
def show_info():
    """Displays information about how to play the game."""
    print(
        "\n **How to Play the Math Challenge Game:**\n"
        "------------------------------------------\n"
        "1️⃣ **Choose a Difficulty Level:**\n"
        "   - Easy: Simple addition problems.\n"
        "   - Medium: Addition and subtraction problems with moderate numbers.\n"
        "   - Hard: More complex addition, subtraction, and multiplication problems.\n"
        "   - Insane: Challenging problems with large numbers and all operators.\n\n"
        "2️⃣ **Choose the Number of Problems:**\n"
        "   - Decide how many problems you'd like to solve in one session.\n\n"
        "3️⃣ **Start Solving:**\n"
        "   - You'll be presented with random math problems based on your chosen difficulty.\n"
        "   - Type the correct answer and hit Enter.\n\n"
        "4️⃣ **Score and Feedback:**\n"
        "   - At the end of the game, you'll see your score, time taken, and correct/wrong answers.\n\n"
        "🎯 **Goal:**\n"
        "   - Aim for the highest accuracy and the fastest time!\n"
        "------------------------------------------\n"
        "🟢 Ready? Choose 'play' from the menu to start the challenge!\n\n"
    )
