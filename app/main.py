import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.classlistservice import ClasslistService
def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기')
    print('2. 로그인')
    print('3. 점수')

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

if __name__ =='__main__':
    main()
    