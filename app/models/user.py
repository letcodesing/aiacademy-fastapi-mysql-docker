class User(object):
    def __init__(self,id,password):
        self.id = id
        self.password = password
        
    def pd(self):
        return self.id

    def sl(self):
        return self.password