# Lab 4: File I/O and CSV Data Processing
#
# Complete this program so that it reads quiz score data from a CSV file,
# cleans the data, computes student averages, and prints a report.
import csv


def clean_score(score_text):
    """
    Convert a score string into an integer.

    If the score is missing or invalid, return None.
    """
    if score_text == "" or score_text == "absent" or score_text == "invalid":
        # Reads the text to check for absent, invalid, or null then return none
        return None
    else:
        return int(score_text)
    # returns it as integer


def calculate_average(scores):
    """
    Calculate the average of a list of numeric scores.

    If the list is empty, return None.
    """
    sum = 0
    count = 0
    # assigns sum and count as 0
    for score in scores:
        if score is not None:
            sum += score
            count += 1
    if count > 0:
        return sum / count
    else:
        return None



def read_scores(filename):
    """
    Read student quiz scores from a CSV file.

    Return a list of dictionaries.

    Each dictionary should contain:
        "name": student name
        "scores": list of valid numeric quiz scores
        "average": student average

    So, the returned list of dictionaries should look like:
    [
        {
            "name": "Alice",
            "scores": [85, 90, 78],
            "average": 84.33
        },
        {
            "name": "Bob",
            "scores": [92, None, 88],
            "average": 90.0
        },
        ...
    ]
    """
    my_list = []
    with open(filename) as csvfile:
        reader = csv.reader(open(filename))
        for row in reader:
            if reader.line_num == 1:
                continue
            else:
                name = row[0]
                scores = [clean_score(row[1]),clean_score( row[2]), clean_score(row[3])]
                average = calculate_average(scores)
            my_list.append({"name": name, "scores": scores, "average": average})
    return my_list



def letter_grade(average):
    """
    Return a simple letter grade based on the average.

    Suggested scale:
        A: average >= 87
        B: average >= 77
        C: average >= 67
        D: average >= 57
        F: otherwise

    If the average is None, return "N/A".
    """
    if average is None:
        return "N/A"
    elif average >= 87:
        return "A"
    elif average >= 77:
        return "B"
    elif average >= 67:
        return "C"
    elif average >= 57:
        return "D"
    else:
        return "F"


def print_student_report(records):
    """
    Print one line of output for each student.
    """
    for record in records:
        print(f'{record["name"]}: Average = {record["average"]:.2f} Grade = {letter_grade(record["average"])}')
    return


def print_class_summary(records):
    """
    Print a summary for the whole class.

    Include:
        number of students
        highest average
        lowest average
    """
    Num = 0
    for record in records:
        Num += record["average"]
    Num /= len(records)

    print("Number of students:", len(records))
    print(f'class average: {Num:.2f}')
    print(f'highest average: {max(record["average"] for record in records):.2f}')
    print(f'lowest average: {min(record["average"] for record in records):.2f}')

def main():
    filename = "../data/quiz_scores.csv"

    # Dict returned as records
    records = read_scores(filename)

    print_student_report(records)
    print()
    print_class_summary(records)


main()
