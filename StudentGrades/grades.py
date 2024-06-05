class Student:
    def __init__(self, name, math_grade, science_grade, english_grade):
        self.name = name
        self.math_grade = math_grade
        self.science_grade = science_grade
        self.english_grade = english_grade

    def compute_average(self):
        total_grades = self.math_grade + self.science_grade + self.english_grade
        return total_grades / 3

    def similarity(self):
        average = self.compute_average()
        if average >= 90:
            return "Excellent"
        elif average >= 80:
            return "Very Good"
        elif average >= 70:
            return "Good"
        elif average >= 60:
            return "Satisfactory"
        else:
            return "Needs Improvement"



name = input("Enter student name: ")
math_grade = float(input("Enter math grade: "))
science_grade = float(input("Enter science grade: "))
english_grade = float(input("Enter English grade: "))


student = Student(name, math_grade, science_grade, english_grade)


print(f"Student: {student.name}")
print(f"Average Grade: {student.compute_average()}")
print(f"Similarity: {student.similarity()}")
