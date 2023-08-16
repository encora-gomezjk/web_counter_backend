
class Words_Reader:

    __lines = []

    def __init__(self):
        lines = []
        with open('data/list_of_words.txt') as f:
            lines = f.read().splitlines()
        self.__lines = lines
    
    def read(self):
        return self.__lines
