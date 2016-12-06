def Linked_List:
    def __init__(self):
        self._A=None
    def __str__(self):
        p = self._A
        while p:
            print(p[0])
            p = p[1]
    def push_front(self,data):
        self._A = [data,self._A]

