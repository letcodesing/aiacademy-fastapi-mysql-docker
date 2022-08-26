from app.models.grade import Grade
class GradeService():
    def __init__(self) -> None:
        self.credit = 0

    def set_grade(self,math,kor,eng):
        grade = Grade(math,kor,eng)
        grade.set_score()
        grade = grade.get_score()
        if grade >= 90:
            self.credit = 'A'
        elif grade >= 80:
            self.credit = 'B'
        elif grade >= 70:
            self.credit = 'C'
        elif grade >= 60:
            self.credit = 'D'
        elif grade >= 50:
            self.credit = 'E'
        else:
            self.credit = 'F'

    def get_grade(self,math,kor,eng):
        self.set_grade(math,kor,eng)
        return self.credit


