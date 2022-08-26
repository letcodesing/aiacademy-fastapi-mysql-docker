class Grade():
    def __init__(self,math,kor,eng):
        self.math = math
        self.kor = kor
        self.eng = eng
        self.mean = 0

    
    def set_score(self):
        self.mean = (self.math + self.kor + self.eng) / 3

    def get_score(self):
        return self.mean