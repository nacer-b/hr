from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(self, b):
        if self.score > b.score:
            return -1
        elif self.score < b.score:
            return 1
        else:
            i = 0
            while i < min(len(self.name), len(b.name)):
                if self.name[i] > b.name[i]:
                    return 1
                elif self.name[i] < b.name[i]:
                    return -1
                else:
                    i+=1
            if len(self.name)<len(b.name):
                return -1
            elif len(self.name)>len(b.name):
                return 1
            else:
                return 0
