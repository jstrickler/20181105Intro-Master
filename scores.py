#!/usr/bin/env python


scores_by_student = {}

with open('DATA/testscores.dat') as scores_in:
    for raw_line in scores_in:
        line = raw_line.rstrip()
        student, raw_score = line.split(':')
        score = int(raw_score)
        if score > 94:
            grade = 'A'
        elif score > 88:
            grade = 'B'
        elif score > 82:
            grade = 'C'
        elif score > 74:
            grade = 'D'
        else:
            grade = 'F'
        scores_by_student[student] = score, grade

print(scores_by_student)
print()

for student, info in sorted(scores_by_student.items()):
    #        0      1    2           0        1        2
    print("{:20s} {:3d} {}".format(student, info[0], info[1]))

#    0  1         0  1
#  "{} {}".format(a, b)
