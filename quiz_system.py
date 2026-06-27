import random

# ==========================================
# 10. Modules / Functions to Create
# ==========================================

def load_questions():
    """
    Returns the question bank as a list of tuples.
    Each tuple holds: (Question, Option A, Option B, Option C, Option D, Correct Answer)
    """
    # Section 11: Minimum 10 unique questions with '#' comments
    return [
        # Question 1
        ("Which data type is IMMUTABLE in Python?", "List", "Dictionary", "Tuple", "Set", "C"),
        # Question 2
        ("What is the correct file extension for Python files?", ".py", ".pyt", ".pt", ".pyw", "A"),
        # Question 3
        ("Which keyword is used to create a function in Python?", "fun", "define", "def", "function", "C"),
        # Question 4
        ("How do you start a for loop in Python?", "for x in y:", "for x to y:", "for x inside y", "loop x in y", "A"),
        # Question 5
        ("Which of the following is an unordered collection?", "List", "Set", "Tuple", "String", "B"),
        # Question 6
        ("What does len() function do?", "Finds length", "Deletes items", "Adds items", "Clears data", "A"),
        # Question 7
        ("Which operator is used for exponentiation?", "^", "**", "pow", "//", "B"),
        # Question 8
        ("How do you insert comments in Python code?", "//", "#", "/*", "<!--", "B"),
        # Question 9
        ("Which method removes whitespaces from both ends?", "strip()", "lower()", "upper()", "split()", "A"),
        # Question 10
        ("What is the output of print(type([]))?", "dict", "tuple", "set", "list", "D")
    ]

def display_question(q_num, q_tuple):
    """Displays a single question with 4 options formatted properly."""
    print(f"\nQ{q_num}: {q_tuple[0]}")
    print(f"  A. {q_tuple[1]:<20} B. {q_tuple[2]}")
    print(f"  C. {q_tuple[3]:<20} D. {q_tuple[4]}")

def get_answer():
    """Accepts and validates student answer input."""
    while True:
        try:
            ans = input("Your Answer: ").strip().upper()
            if ans not in ['A', 'B', 'C', 'D']:
                raise ValueError("Invalid choice! Only A, B, C, or D accepted.")
            return ans
        except ValueError as e:
            print(f"❌ {e}")

def evaluate_quiz(question_bank):
    """Loops through questions, checks answers, and tracks mistakes."""
    score = 0
    wrong_answers = [] 
    
    shuffled_bank = list(question_bank)
    random.shuffle(shuffled_bank)
    
    for idx, q_tuple in enumerate(shuffled_bank, 1):
        display_question(idx, q_tuple)
        user_ans = get_answer()
        correct_ans = q_tuple[5]
        
        if user_ans == correct_ans:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Incorrect!")
            wrong_answers.append((q_tuple[0], user_ans, correct_ans))
            
    return score, wrong_answers, len(shuffled_bank)

def calculate_grade(percentage):
    """Returns grade scale based on performance percentage."""
    if percentage >= 90: return 'A+'
    elif percentage >= 80: return 'A'
    elif percentage >= 70: return 'B'
    elif percentage >= 50: return 'C'
    else: return 'F'

def show_report(name, roll, score, total, percentage, grade):
    """Prints final performance breakdown matching screenshot Sample Output exactly."""
    print("\n====== RESULT REPORT ======")
    print(f"Name    : {name}")
    print(f"Roll    : {roll}")
    print(f"Score   : {score} / {total}")
    print(f"Percent : {percentage:.2f}%")
    print(f"Grade   : {grade}")
    print(f"Result  : {'PASS' if percentage >= 50 else 'FAIL'}")
    print("***************************")

def show_wrong_answers(wrong_answers):
    """Displays incorrectly answered review list at the very end."""
    if wrong_answers:
        print("\n--- Review of Wrong Answers ---")
        for idx, item in enumerate(wrong_answers, 1):
            q_text, user_choice, correct_choice = item
            print(f"{idx}. {q_text}")
            print(f"   Your Answer: {user_choice} | Correct Answer: {correct_choice}")
    else:
        print("\n🎉 Perfect score! No wrong answers to review.")

# ==========================================
# 8. Flow of Execution (Main Core)
# ==========================================
def main():
    print("----- PYTHON QUIZ SYSTEM -----")
    
    name = input("Student Name: ").strip()
    while True:
        try:
            roll = int(input("Roll: "))
            break
        except ValueError:
            print("❌ Invalid input! Roll number must be an integer.")
            
    print(f"\nStudent: {name} | Roll: {roll}")
    
    question_bank = load_questions()
    score, wrong_answers, total = evaluate_quiz(question_bank)
    
    percentage = (score / total) * 100
    grade = calculate_grade(percentage)
    
    show_report(name, roll, score, total, percentage, grade)
    show_wrong_answers(wrong_answers)
    
    print("\nEXIT. Thank you for taking the examination!")

if __name__ == "__main__":
    main()