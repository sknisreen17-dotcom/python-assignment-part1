# Task 1: Data Parsing & Profile Cleaning

# This is our starting list of messy data
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# We create an empty list to store our cleaned-up data
cleaned_students = []

# Loop through each student in the raw list one by one
for student in raw_students:
    
    # 1. Clean the name: Remove extra spaces and make it Title Case
    clean_name = student["name"].strip().title()
    
    # 2. Convert the roll number from text ("101") to a real number (101)
    clean_roll = int(student["roll"])
    
    # 3. Convert marks_str to a list of numbers
    # First, we split the long string into a list of smaller strings
    marks_list_strings = student["marks_str"].split(", ")
    # Then, we turn those small strings into actual integers
    clean_marks = []
    for m in marks_list_strings:
        clean_marks.append(int(m))

    # 4. Check if the name is valid (contains only letters and spaces)
    # We remove the space temporarily to check if everything else is alphabetic
    if clean_name.replace(" ", "").isalpha():
        name_status = "✓ Valid name"
    else:
        name_status = "✗ Invalid name"

    # 5. Print the formatted Profile Card using f-strings
    print("=" * 32)
    print(f"Student : {clean_name} ({name_status})")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print("=" * 32)
    
    # Save this cleaned info into our new list for later use
    cleaned_students.append({
        "name": clean_name, 
        "roll": clean_roll, 
        "marks": clean_marks
    })

# Final Step: Find student 103 and print name in ALL CAPS and lowercase
print("\n--- Special Report for Roll 103 ---")
for s in cleaned_students:
    if s["roll"] == 103:
        print("UPPERCASE:", s["name"].upper())
        print("lowercase:", s["name"].lower())



# Task 2: Marks Analysis and Interactive Entry
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"--- Analysis for {student_name} ---")

# Loop through the list using an index (i)
for i in range(len(subjects)):
    m = marks[i]
    sub = subjects[i]
    
    # Determine the grade
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"
        
    print(f"{sub}: {m} ({grade})")

# Calculations
total = sum(marks)
avg = round(total / len(marks), 2)

# Finding Highest and Lowest
# We use the index of the max/min mark to find the subject name
high_idx = marks.index(max(marks))
low_idx = marks.index(min(marks))

print(f"\nTotal Marks: {total}")
print(f"Average: {avg}")
print(f"Highest: {subjects[high_idx]} ({marks[high_idx]})")
print(f"Lowest: {subjects[low_idx]} ({marks[low_idx]})")

print("\n--- New Subject Entry (Type 'done' to finish) ---")
new_count = 0

while True:
    sub_input = input("Enter subject name: ").strip()
    
    if sub_input.lower() == "done":
        break
    
    marks_input = input(f"Enter marks for {sub_input}: ")
    
    try:
        # Try to convert input to a number
        m_val = float(marks_input)
        
        # Check if it's in the valid range 0-100
        if 0 <= m_val <= 100:
            subjects.append(sub_input)
            marks.append(m_val)
            new_count += 1
        else:
            print("⚠️ Warning: Marks must be between 0 and 100.")
            
    except ValueError:
        # This runs if the user typed letters instead of a number
        print("⚠️ Warning: Please enter a valid numeric value.")

# Final Summary
updated_avg = round(sum(marks) / len(marks), 2)
print(f"\nAdded {new_count} new subjects.")
print(f"New Updated Average: {updated_avg}")



# Task 3: Class Performance Summary

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# Variables to keep track of class-wide stats
pass_count = 0
fail_count = 0
all_averages = []
topper_name = ""
topper_avg = 0

# Print the Header
print(f"{'Name':<18} | {'Average':<7} | {'Status'}")
print("-" * 40)

# Loop through the data
for name, marks in class_data:
    # 1. Compute individual average
    avg = round(sum(marks) / len(marks), 2)
    all_averages.append(avg)
    
    # 2. Determine Pass/Fail status
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1
        
    # 3. Check if this student is the topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
        
    # 4. Print the row (formatted for alignment)
    print(f"{name:<18} |  {avg:<7.2f} | {status}")

# Final Summary Report
class_total_avg = round(sum(all_averages) / len(all_averages), 2)

print("-" * 40)
print(f"Passed: {pass_count} | Failed: {fail_count}")
print(f"Class Topper  : {topper_name} ({topper_avg})")
print(f"Overall Class Average: {class_total_avg}")



# Task 4: String Manipulation Utility

# The original messy essay
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# 1. Strip whitespace
# This removes the empty spaces at the very start and very end
clean_essay = essay.strip()
print(f"Step 1 (Stripped): '{clean_essay}'")

# 2. Convert to Title Case
# Capitalizes the first letter of every word
title_essay = clean_essay.title()
print(f"\nStep 2 (Title Case):\n{title_essay}")

# 3. Count "python" (Case-insensitive)
# Since clean_essay is already lowercase, we can count directly
python_count = clean_essay.count("python")
print(f"\nStep 3 (Count of 'python'): {python_count}")

# 4. Replace "python" with "Python 🐍"
emoji_essay = clean_essay.replace("python", "Python 🐍")
print(f"\nStep 4 (Replacement):\n{emoji_essay}")

# 5. Split into sentences
# We look for the pattern ". " to find where sentences end
sentences = clean_essay.split(". ")
print(f"\nStep 5 (Split List):\n{sentences}")

# 6. Numbered sentences with proper ending
print("\nStep 6 (Formatted Sentences):")
for i in range(len(sentences)):
    sentence = sentences[i].strip()
    
    # Check if the sentence already ends with a period
    if not sentence.endswith("."):
        sentence = sentence + "."
        
    # Print with a number (i + 1 because lists start at 0)
    print(f"{i + 1}. {sentence}")