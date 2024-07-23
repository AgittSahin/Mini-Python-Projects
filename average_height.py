# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0
number = 0
for i in student_heights:
  sum += i
for i in student_heights:
  number += 1
print(f"total height = {sum}")
print(f"total height = {number}")