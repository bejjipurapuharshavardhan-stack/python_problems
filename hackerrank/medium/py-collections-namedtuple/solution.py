from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
total_marks = 0

for _ in range(n):
    row = input().split()
    student = Student(*row)
    total_marks += int(student.MARKS)

print(f"{total_marks / n:.2f}")
