class Grade2(object):
    def __init__(self) -> None:
        self.avg = 0

    def set_score(self,math,kor,eng):
        self.avg = (math+kor+eng)/3

    def get_score(self):
        return self.avg

    def get_name(self,name):
        return name