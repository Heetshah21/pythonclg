"""3. Student Weighted Score Calculator
Problem Statement
You are given a list of students:

Task:
• Keep students whose average is ≥ 60
• Increase each mark by 5 grace marks
• Compute the total of all updated marks
Input
students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]

Output: 
375"""
def main():
    students = [
        {"name": "A", "marks": [50, 60, 70]},
        {"name": "B", "marks": [30, 40]},
        {"name": "C", "marks": [80, 90]}
    ]
    valid_students = filter(lambda s: sum(s["marks"])/len(s["marks"]) >= 60, students)
    updated_marks = map(lambda s: list(map(lambda m: m+5, s["marks"])), valid_students)
    total_updated_marks = sum(map(lambda s: sum(s), updated_marks))
    print(total_updated_marks)
if __name__=="__main__":
    main()