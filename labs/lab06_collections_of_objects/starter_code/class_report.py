# Lab 6: Collections of Objects

from student_record import StudentRecord
import csv

def clean_score(score_text):
    """
    Convert score text to an integer.

    Return None if the score is missing or invalid.
    """
    if score_text == "" or score_text == "absent" or score_text == "invalid":
        return None
    else:
        return int(score_text)


def read_student_records(filename):
    """
    Read the CSV file and return a list of StudentRecord objects.
    """
    my_list = []
    with open(filename) as csvfile:
        reader = csv.reader(open(filename))
        for row in reader:
            if reader.line_num == 1:
                continue
            else:
                scores = [clean_score(row[2]), clean_score(row[3]), clean_score(row[4])]
                studentrecord = StudentRecord(row[1], row[0])
                studentrecord.scores = scores
                my_list.append(studentrecord)
    return(my_list)



def class_average(students):
    """
    Return the average of all student averages.

    Ignore students with no valid scores.
    """
    avg = 0.0
    count = 0
    for student in students:
        average = student.calculate_average()
        if average is not None:
            avg += average
            count += 1
    if count > 0:
        return avg / count
    else:
        return None





def find_highest_average_student(students):
    """
    Return the StudentRecord object with the highest average.
    """
    max_list = 0
    highest_student = None
    for student in students:
        student_average = student.calculate_average()
        if student_average > max_list:
            highest_student = student
            max_list = student_average
    return highest_student





def find_lowest_average_student(students):
    """
    Return the StudentRecord object with the lowest average.
    """
    min_list=100
    lowest = None
    for student in students:
        student_average = student.calculate_average()
        if student_average < min_list:
            lowest = student
            min_list = student_average
    return lowest


def print_class_report(students):
    """
    Print all student records and a class summary.
    """
    for student in students:
        print(student)
    print(f"class average: {class_average(students):.2f}")
    highest_student = find_highest_average_student(students)
    if highest_student is not None:
        print(f"Highest average: {highest_student.name} with {highest_student.calculate_average():.2f}")
    lowest_student = find_lowest_average_student(students)
    if lowest_student is not None:
        print(f'Lowest average: {lowest_student.name} with {lowest_student.calculate_average():.2f}')


def main():
    students = read_student_records("../data/student_scores.csv")
    print_class_report(students)


main()
