#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    rounded_grades = []

    for grade in grades:
        if grade < 38:
            # If the grade is less than 38, no rounding occurs
            rounded_grades.append(grade)
        else:
            # Calculate the next multiple of 5 greater than or equal to the grade
            next_multiple_of_5 = (grade // 5 + 1) * 5

            # If the difference between the next multiple and the grade is less than 3, round up
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                # Otherwise, keep the original grade
                rounded_grades.append(grade)

    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
