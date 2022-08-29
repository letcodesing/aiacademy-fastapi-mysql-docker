from email import iterators
import os
import sys
from more_itertools import iterate
from numpy import iterable

from tqdm import tqdm

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))
from app.services.grade2 import Grade2Service
from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.classlistservice import ClasslistService
from app.services.grade import GradeService
from app.services.pandas_quiz1 import PandasQuiz
def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기')
    print('2. 로그인')
    print('3. 점수')
    print('4. 학점')
    print('5. 판다스퀴즈')
    print('6. 학점2')

    menu = input('메뉴')
    return menu

def main():
    
    while 1:
        menu = print_menu()

        if menu == '0':
            print('종료')
            break

        elif menu == '1':
            calcul = CalculatorService()
            first = int(input('첫째값'))
            second = int(input('둘째'))
            calcul.calculate(first,second)

        elif menu == '2':
            loging = UserService()
            id = str(input('아이디'))
            password = str(input('비번'))
            loging.login(id,password)
            
        elif menu =='3':
            list = ClasslistService()
            z = str(input('이름'))
            x = int(input('수학'))
            c = int(input('영어'))
            v = int(input('과학'))
            print(f'{z}의 등급은')
            list.listService(x,c,v)


        elif menu == '4':
            puncher = GradeService()
            name = str(input('이름'))
            math = int(input('math'))
            eng = int(input('eng'))
            kor = int(input('kor'))

            print(f'{name}의 학점은 {puncher.get_grade(math,eng,kor)}')
            
        elif menu == '5':
            quiz = PandasQuiz()
            while 1:
                quiz_num = input('퀴즈번호1~4, 종료는 9')
                if quiz_num == '0':
                    break
                elif quiz_num == '1':
                    quiz.quiz1()
                elif quiz_num == '2':
                    quiz.quiz2()
                elif quiz_num == '3':
                    quiz.quiz3()
                elif quiz_num == '4':
                    quiz.quiz4()
                


        elif menu == '6':
            name = str(input('name'))        
            math = int(input('math'))
            kor = int(input('kor'))
            eng = int(input('eng'))
            grader = Grade2Service()
            print(f'name:{grader.get_name(name)}의 학점은 {grader.get_grade(math,kor,eng)}입니다')                

if __name__ =='__main__':
    main()

    enumerate
    tqdm
    iterable
    iterators
    