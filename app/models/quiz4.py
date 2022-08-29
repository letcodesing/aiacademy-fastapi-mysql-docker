import random
import string


class Quiz4():
    def __init__(self) -> None:
        pass

    def get_starlist(self):
        rand_str = ''
        for i in range(5):
            strlist = []
            rand_str += str(random.choice(string.ascii_letters))
            strlist.append(rand_str)
        return strlist[0]