import random

# Define questions for each category and level
questions = {
    "beginner": {
        "physics": [
            ("What is the speed of light?", "300000 km/s"),
            ("What is the unit of force?", "Newton"),
            ("What is the formula for calculating velocity?", "v = u + at"),
            ("Who discovered gravity?", "Isaac Newton"),
            ("What is the unit of power?", "Watt"),
            ("What is the gravitational acceleration on Earth?", "9.8"),
            ("What is the unit of electric current?", "Ampere"),
            ("What is the first law of motion?", "Inertia"),
            ("What is the SI unit of temperature?", "Kelvin"),
            ("What is the main gas in the sun?", "Hydrogen")
        ],
        "chemistry": [
            ("What is the chemical symbol for water?", "H2O"),
            ("What is the atomic number of oxygen?", "8"),
            ("Who discovered the electron?", "J.J. Thomson"),
            ("What is the periodic table?", "Arrangement of elements"),
            ("What is the chemical symbol for gold?", "Au"),
            ("What is the pH of pure water?", "7"),
            ("What is the chemical formula for carbon dioxide?", "CO2"),
            ("What is the chemical symbol for sodium?", "Na"),
            ("What is the main gas in Earth's atmosphere?", "Nitrogen"),
            ("What is the pH range of acids?", "0 to 7")
        ],
        "mathematics": [
            ("What is 2+2?", "4"),
            ("What is the square root of 9?", "3"),
            ("What is 10 divided by 2?", "5"),
            ("What is 3*3?", "9"),
            ("What is 100/10?", "10"),
            ("What is the value of pi?", "3.14"),
            ("What is 12% of 100?", "12"),
            ("What is the next prime number after 7?", "11"),
            ("What is 5 squared?", "25"),
            ("What is 7+8?", "15")
        ],
        "python programming": [
            ("What function is used to print in Python?", "print()"),
            ("What is the symbol for comments in Python?", "#"),
            ("What is the correct file extension for Python files?", ".py"),
            ("How do you create a list in Python?", "[]"),
            ("What does 'len()' function do?", "Gets length"),
            ("How do you create a function in Python?", "def function_name():"),
            ("What is a variable?", "Storage for data"),
            ("What is a for loop?", "Loop over items"),
            ("How do you start a while loop?", "while condition:"),
            ("How do you import a module?", "import module_name")
        ],
        "general knowledge": [
            ("What is the capital of Bangladesh?", "Dhaka"),
            ("Who is the founder of Bangladesh?", "Sheikh Mujibur Rahman"),
            ("When did Bangladesh gain independence?", "1971"),
            ("What is the currency of Bangladesh?", "Taka"),
            ("Which language is spoken in Bangladesh?", "Bengali"),
            ("What is the national flower of Bangladesh?", "Water lily"),
            ("What is the largest river in Bangladesh?", "Padma"),
            ("What is the national sport of Bangladesh?", "Kabaddi"),
            ("What is the longest beach in Bangladesh?", "Cox's Bazar"),
            ("Who was the first President of Bangladesh?", "Sheikh Mujibur Rahman")
        ]
    }
}

# Function to ask questions from a specific category and level
def ask_questions(level, category):
    score = 0
    random.shuffle(questions[level][category])
    for question, answer in questions[level][category]:
        user_answer = input(f"{question} ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")
    return score

# Main quiz game function
def quiz_game():
    print("Welcome to the Quiz Game!")
    name = input("Please enter your name: ")
    print(f"Hello {name}! Let's start the quiz.")

    levels = ["beginner"]
    categories = ["physics", "chemistry", "mathematics", "python programming", "general knowledge"]

    total_score = 0

    # Loop through levels
    for level in levels:
        print(f"\nStarting {level.capitalize()} Level Questions:")
        # Loop through categories
        for category in categories:
            print(f"\nCategory: {category.capitalize()}")
            score = ask_questions(level, category)
            total_score += score
            print(f"Your score for {category.capitalize()} in {level.capitalize()} level: {score}/10")

    print(f"\nThank you for playing, {name}!")
    print(f"Your total score is: {total_score}/150")

# Start the game
quiz_game()
