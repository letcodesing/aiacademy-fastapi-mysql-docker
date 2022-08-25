from app.models.calculator import Calculator
class CalculatorService(object):
    def __init__(self) ->None:
        pass

    def calculate(self,firt,sec):
        calculator = Calculator(firt,sec)
        print(f'첫째수:{calculator.firt}')
        print(f'둘째수:{calculator.sec}')
        print(f'{calculator.firt}+{calculator.sec}={calculator.sum()}')
        print(f'{calculator.firt}-{calculator.sec}={calculator.sub()}')
        print(f'{calculator.firt}*{calculator.sec}={calculator.multiple()}')
        print(f'{calculator.firt}/{calculator.sec}={calculator.devide()}')