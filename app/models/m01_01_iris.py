import tensorflow as tf
tf.random.set_seed(137)
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.callbacks import EarlyStopping
from sklearn.svm import LinearSVC #리니어 서포트 벡터 
from sklearn.metrics import accuracy_score

ES = EarlyStopping(monitor='val_loss', mode='min', patience=20, restore_best_weights=True)

class Iris:

    def __init__(self) -> None:
        self.datasets = None
        self.x_train = None
        self.y_trian = None
        self.x_test = None
        self.y_test = None
        self.model = None
    
    def hook(self):
        self.from_csv()
        self.preprocessing()
        self.learning()
        self.test()

# ___2.1.3. 모델의 선정과 파라미터 정리
    def from_csv(self):
        self.datasets = load_iris()
        

# ___2.1.4. 전처리
    def preprocessing(self):
        datasets = self.datasets
        x = datasets['data']
        y = datasets['target']        
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x,y, train_size=0.7, shuffle=True, random_state=137)
        self.missing_value_process()

    def missing_value_process(self):
        pass

# ___2.1.5. 학습
    def learning(self):
        self.model = LinearSVC()
        self.model.fit(self.x_train,self.y_train)
        

# ___2.1.6. 평가
    def test(self):
        result = self.model.score(self.x_test,self.y_test)
        print(result)






