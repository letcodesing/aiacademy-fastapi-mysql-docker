from app.models.classlist import ClassList
class ClasslistService():
    def __init__(self) -> None:
        pass

    def listService(self,w,e,r):
        lister = ClassList(w,e,r)
        if lister.lister() >=100:
            print('A')
        elif 80<= lister.lister() < 100:
            print('B')
        elif 60<= lister.lister() <80:
            print('C')
        elif 40 <= lister.lister() <60:
            print('D')
        elif 20<=lister.lister() <40:
            print('E')