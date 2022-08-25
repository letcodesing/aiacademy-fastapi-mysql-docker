from app.models.user import User

class UserService(object):
    def __init__(self) -> None:
        pass

    def login(self,id,password):
        
        logi = User(id,password)
        print(f'아이디{logi.pd()},비번{logi.sl()}')
