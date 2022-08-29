import random
from icecream import ic
import pandas as pd
from app.models.quiz4 import Quiz4
import string
import numpy as np
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

    def get_id(self):
        return [''.join(random.choice(string.ascii_letters)) for i in range(5)]

    def get_score(self):
        return np.random.randint(0,100,(10,4))


    def quiz4(self):
        name = self.get_id()
        df = pd.DataFrame(self.get_score(),
                         index = self.get_id(),
                         columns = ['국','수','영','사'])

         
   
        
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