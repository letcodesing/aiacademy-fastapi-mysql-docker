# from app.models.quiz4 import Quiz4
import pandas as pd
import random
# get = Quiz4()
stay = pd.DataFrame(orient=f'9',columns=['국어','영어','수학','사회'])

df =pd.DataFrame.from_dict(
            {f'3':[i for i in random.sample(range(random.randint(10,100)),4)]}
        )
print(stay)
# print({f'{i for i in (10)}':[i for i in random.sample(range(random.randint(10,100)),4)]})

# for i in range(10):
#     stay.loc[i] = {f'{get.get_starlist()}':[i for i in random.sample(range(random.randint(10,100)),4)]}