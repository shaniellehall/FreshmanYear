exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 100):\n'))
overall_grade = (exam1_grade + exam2_grade + exam3_grade + exam4_grade) / 4
print('Your overall grade is:', overall_grade)