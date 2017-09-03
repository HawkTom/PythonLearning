
class queue(object):
    def __init__(self):
        self.que = []
        self.size = len(self.que)

    def input(self,element):
        self.que.append(element)
        self.size += 1

    def output(self):
        self.que.pop(0)
        self.size -= 1

