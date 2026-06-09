# Lab 6: Collections of Objects
#
# Complete this class. You may reuse ideas from Lab 5.


class StudentRecord:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        if score > 0 or score < 100:
            self.scores.append(score)
        else:
            self.scores.append("")

    def calculate_average(self):
        avg = 0.0
        total = 0
        for score in self.scores:
            if score == None:
                pass
            else:
                avg+= score
                total += 1
        return avg / total

    def highest_score(self):
        if self.scores == []:
            return None
        else:
            return max(self.scores)


    def lowest_score(self):
        if self.scores == []:
            return None
        else:
            return min(self.scores)

    def letter_grade(self):
        if self.calculate_average() >= 87:
            return ("A")
        elif self.calculate_average() >= 77:
            return("B")
        elif self.calculate_average() >= 67:
            return("C")
        elif self.calculate_average() >= 57:
            return("D")
        else:
            return("F")

    def __str__(self):
        return (f"studentrecord(name={self.name}, student_id={self.student_id} scores= {self.scores}")
