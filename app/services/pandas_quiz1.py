import random
from icecream import ic
import pandas as pd
from app.models.quiz4 import Quiz4
class PandasQuiz():
    def __init__(self) -> None:
        pass

    def quiz1(self):
        df = pd.DataFrame.from_dict(
        {'1' : [1,  3,  5], '2' : [2,  4,  6]}, orient='index', columns=['a','b','c'])            
        ic(df)

    def quiz2(self):
        df = pd.DataFrame.from_dict(
            {'1':[1,2,3],'2':[4,5,6],'3':[7,8,9],'4':[10,11,12]},orient='index',columns=['A','B','C']
        )
        ic(df)

    def quiz3(self):
        df = pd.DataFrame.from_dict(
            {'0':[i for i in random.sample(range(random.randint(10,100)),3)],'1':[i for i in random.sample(range(random.randint(10,100)),3)]},orient='index',columns=['0','1','2']
        )
        ic(df)

    def quiz4(self):
        get = Quiz4()
        stay = pd.DataFrame(orient=f'{get.get_starlist()}',columns=['국어','영어','수학','사회'])
        df =pd.DataFrame.from_dict(
            {f'{get.get_starlist()}':[i for i in random.sample(range(random.randint(10,100)),4)]},orient='index',columns=['국어','영어','수학','사회']
        )
        d = {f'{get.get_starlist()}':[c for c in random.sample(range(random.randint(10,100)),4)]}
        for i in range(10):
            stay.loc[i] = d
            
         
   
        
        ic(stay)
    '''
    Q1. 다음 결과 출력
        a  b  c
    1  1  3  5
    2  2  4  6
    ic| df1:    a  b  c
                1  1  3  5
                2  2  4  6
    '''