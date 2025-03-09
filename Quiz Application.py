'''
      
            Name : Antuley Aman Siraj
            Roll No : 23CO25
            Batch - 01


                *Mini-Project*
            Topic : Quiz Application

'''


quiz_questions = {
    "What is the capital of France?": "Paris",
    "which is the Largest Country on Earth" : "China",
    "Which planet is known as the Red Planet?": "Mars",
    "Who developed the theory of relativity?": "Einstein",
    "What is the largest ocean on Earth?": "Pacific",
    "What is 5 + 7?": "12"
}

def start_quiz():
    score = 0  # Initialize score
    total_questions = len(quiz_questions)

    print("\n Welcome to the Quiz!\n")

    for question, correct_answer in quiz_questions.items():
        print(question)
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f" Incorrect! The correct answer is: {correct_answer}\n")

    print(f" Quiz Completed! Your Score: {score}/{total_questions}")
    print("Thank you for playing!\n")

# Run the Quiz
start_quiz()


# Conclusion : 