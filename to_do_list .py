LOW = 0
MED = 1
HI = 2
class to_do:
    def __init__(self, task_list = None):
        self.count = 0
        self.to_do = {}
        if task_list != None:
            for item in task_list:
                self.to_do[count] = [item,LOW]
