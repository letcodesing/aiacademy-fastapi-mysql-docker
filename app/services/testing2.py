import pandas as pd
import random 
list = []
for i in range(1,10):
    df = pd.DataFrame.from_dict({'0':[i for i in random.sample(range(random.randint(10,100)),3)],'1':[i for i in random.sample(range(random.randint(10,100)),3)]},orient='index',columns=['0','1','2'])
    df.loc[i+10] = {'0':[i for i in random.sample(range(random.randint(10,100)),3)],'1':[i for i in random.sample(range(random.randint(10,100)),3)]}
    
print(df)