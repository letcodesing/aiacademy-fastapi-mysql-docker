from app.models.grade2 import Grade2
class Grade2Service(object):
    def __init__(self) -> None:
        self.grade = 0

    def making_grade(self,math,kor,eng):
        score = Grade2()
        score.set_score(math,kor,eng)
        grader = score.get_score()
        if grader >= 90:
            self.grade = 'A'
        elif grader >=80:
            self.grade = 'B'
        elif grader >=70:
            self.grade = 'C'
        elif grader >=60:
            self.grade = 'D'
        elif grader >=50:
            self.grade = 'E'
        else:
            self.grade = 'F'
    
    def get_grade(self,math,kor,eng):
        self.making_grade(math,kor,eng)
        return self.grade

    def get_name(self,name):
        namer = Grade2()
        return namer.get_name(name)