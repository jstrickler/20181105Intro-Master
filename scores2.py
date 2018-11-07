#!/usr/bin/env python

def main():
    scores_by_student = read_data()

    for student, score in sorted(scores_by_student.items()):
        print("{:20s} {:3d} {}".format(student, score, calculate_grade(score)))


def calculate_grade(score):
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

    return grade


def read_data():
    data = {}

    with open('DATA/testscores.dat') as scores_in:
        for raw_line in scores_in:
            line = raw_line.rstrip()
            student, raw_score = line.split(':')
            score = int(raw_score)
            data[student] = score
    return data

main()
