import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService

def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기')
    menu = input('메뉴')
    return menu

def main():
    print_menu()
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
if __name__ =='__main__':
    main()
    