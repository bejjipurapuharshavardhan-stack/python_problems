# 1. Get the number of students (N) and subjects (X)
first_line = input().split()
N = int(first_line[0])
X = int(first_line[1])

# 2. Read the scores for each subject and save them
all_scores = []
for i in range(X):
    subject_marks = list(map(float, input().split()))
    all_scores.append(subject_marks)

# 3. zip(*all_scores) groups each student's marks together
for student_marks in zip(*all_scores):
    total_score = sum(student_marks)
    average = total_score / X
    print(average)
