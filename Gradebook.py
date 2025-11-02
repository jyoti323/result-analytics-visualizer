import csv
import os

def main():
    print("Welcome to GradeBook Analyzer")
    print("1. Manual Entry")
    print("2. Load from CSV")
    print("3. Exit")
    
    while True:
        choice = input("\nChoose option (1-3): ")
        
        if choice == '1':
            manual_entry()
        elif choice == '2':
            csv_entry()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def manual_entry():
    marks = {}
    print("\nEnter student data (type 'done' to finish):")
    
    while True:
        name = input("Name: ")
        if name.lower() == 'done':
            break
        try:
            score = int(input("Marks: "))
            if 0 <= score <= 100:
                marks[name] = score
            else:
                print("Marks must be 0-100.")
        except:
            print("Invalid marks.")
    
    if marks:
        analyze(marks)
    else:
        print("No data entered.")

def csv_entry():
    marks = {}
    filename = input("\nEnter CSV filename: ")
    
    if not os.path.exists(filename):
        print("File not found.")
        return
    
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    name, score = row[0].strip(), row[1].strip()
                    try:
                        marks[name] = int(score)
                    except:
                        continue
        if marks:
            analyze(marks)
        else:
            print("No valid data in CSV.")
    except:
        print("Error reading file.")

def analyze(marks):
    if not marks:
        return
    
    scores = list(marks.values())
    names = list(marks.keys())
    
    avg = sum(scores) / len(scores)
    sorted_scores = sorted(scores)
    n = len(scores)
    median = sorted_scores[n//2] if n % 2 else (sorted_scores[n//2-1] + sorted_scores[n//2]) / 2
    max_score = max(scores)
    min_score = min(scores)
    
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    
    grade_count = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for g in grades.values():
        grade_count[g] += 1
    
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    
    print("\n" + "="*40)
    print("GRADEBOOK SUMMARY")
    print("="*40)
    print(f"Total Students: {len(marks)}")
    print(f"Average: {avg:.2f}")
    print(f"Median: {median}")
    print(f"Highest: {max_score}")
    print(f"Lowest: {min_score}")
    print("-"*40)
    print("Grade Distribution:")
    for g in 'ABCDF':
        print(f"  {g}: {grade_count[g]}")
    print("-"*40)
    print(f"Passed (>=40): {len(passed)}")
    print(f"Failed (<40): {len(failed)}")
    print("="*40)
    
    print("\nName       Marks    Grade")
    print("-" * 30)
    for name in names:
        score = marks[name]
        grade = grades[name]
        print(f"{name:<10} {score:>5}    {grade:>5}")
    print("-" * 30)

if __name__ == "__main__":
    main()
    