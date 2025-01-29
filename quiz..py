#import time allows me to use pythons time related functions so I can create a countdown in my quiz
import time

def greeting():
    print("Welcome to the Ultimate Quiz Game!")
    print("-" * 30)  # Add a separator so it looks neat
    username = input("Insert Username: ")
    print(f"\nHello {username} 🌟 and welcome to my Quiz game")
    print("This quiz will test your knowledge in Python! Get ready to challenge yourself!")

    #\n helps for visual clarity as it makes a new line to separate the text

    #use while loop so the user can come back when they are ready and they do not have to start the whole code again
    ready = ""
    while ready != "yes":
        ready = input("\nAre you ready to start? (yes/no): ").strip().lower()
        if ready == "no":
            print("No problem! Let me know when you're ready. 😊")
        elif ready != "yes":
            print("Please answer 'yes' or 'no'.")

    print("\nGreat! Let's begin in...")
    for i in range(3, 0, -1):
        print(i)
        #.sleep slows down the time by adding one second intervals before showing the next number
        time.sleep(1)
    print("\nGo! 🚀")


greeting()

questions = [
    {
        "question": "1. What is the correct syntax to output 'Hello, World!' in Python?",
        "options": ["echo('Hello, World!')", "print('Hello, World!')", "output('Hello, World!')", "printf('Hello, World!')"],
        "correct_answer": 2
    },
    {
        "question": "How do you create a variable in Python?",
        "options": ["var x = 5", "x = 5", "let x = 5", "int x = 5"],
        "correct_answer": 2
    },
    {
        "question": "Which one is NOT a legal variable name?",
        "options": ["my_var", "_myvar", "Myvar", "my-var"],
        "correct_answer": 3
    },
    {
        "question": "4. Which function is used to get the length of a list in Python?",
        "options": ["list_len()", "len()", "length()", "size()"],
        "correct_answer": 2  
    },
    {
        "question": "5. How do you define a function in Python?",
        "options": ["function my_function():", "def my_function[]:", "def my_function():", "func my_function()"],
        "correct_answer": 3 
    },
    {
        "question": "6. Which of the following is used to import a module in Python?",
        "options": ["import module_name", "include module_name", "use module_name", "load module_name"],
        "correct_answer": 1  
    },
    {
        "question": "7. How do you check the type of a variable in Python?",
        "options": ["type(variable)", "check(variable)", "isinstance(variable)", "getType(variable)"],
        "correct_answer": 1  
    },
    {
        "question": "8. Which of these is a correct way to write a comment in Python?",
        "options": ["// This is a comment", "# This is a comment", "/* This is a comment */", "<!-- This is a comment -->"],
        "correct_answer": 2 
    },
    {
        "question": "9. What will be the output of the following code?\n\nx = 10\ny = 5\nprint(x % y)",
        "options": ["10", "5", "0", "None"],
        "correct_answer": 3  
    },
    {
        "question": "10. How do you create a list in Python?",
        "options": ["list = {1, 2, 3}", "list = [1, 2, 3]", "list = (1, 2, 3)", "list = 1, 2, 3"],
        "correct_answer": 2  
    }
]

#Set the score to 0
def quiz():
    score = 0
    #enumerate will count the index of questions and options that I have stored in the dictionary questions
    for idx, q in enumerate(questions):
        print(f"Q{idx + 1}: {q['question']}")  # Display the question number and text

        print("-" * 30)

        #display the options with their corresponding numbers
        for i, option in enumerate(q["options"], 1): 
            print(f"{i}. {option}")

        user_answer = None  # Initialize as None to indicate no valid input yet
        while user_answer is None:  # Keep asking until the user provides a valid input
            try:
                #ask the user for their answer
                user_input = input("Please select the correct option (1-4): ").strip()
                user_answer = int(user_input)  # Convert input to an integer
                
                #check if the input is valid range
                if user_answer < 1 or user_answer > 4:
                    print("Invalid option, please choose a number between 1 and 4.")
                    user_answer = None
            except ValueError:
                #understand the user has input an invalid answer and ask them to try again
                print("Invalid input! Please enter a number.")
        
        
        if user_answer == q["correct_answer"]:
            print("Correct! ✅")
            score += 1  
        else:
            
            print(f"Wrong! The correct answer was option {q['correct_answer']}.\n")
        
        print()  # Add a blank line for readability between questions

    #final score and results
    print(f"Your total score is: {score}/{len(questions)}")
    
    #feedback
    if score == len(questions):
        print("Excellent! You got all answers correct! 🌟")
    elif score >= len(questions) // 2:
        print("Good job! You did well. 👍")
    else:
        print("Better luck next time! Keep practicing! 💪")

    print("\nThank you for playing the Ultimate Quiz Game! We hope you enjoyed it. 😊")

    
quiz()