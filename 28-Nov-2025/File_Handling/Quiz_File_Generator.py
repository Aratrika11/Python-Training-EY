"""8. Quiz File Generator
 Write a function that takes a list of questions and writes them into quiz.txt with question numbers.
 Include blank lines for answers."""

def generate_quiz(questions):
    with open("quiz.txt","w")as f:
        for i,q in enumerate(questions,1):
            f.write(f"{i}.{q}\n")
            f.write("\n")

questions_list = [
    "What is the capital of India?",
    "Who is the current F1 WDC?",
    "Which is the largest planet in our solar system?"
]
generate_quiz(questions_list)
print("Quiz Generated")