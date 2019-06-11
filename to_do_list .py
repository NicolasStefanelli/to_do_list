LOW = 0
MED = 1
HI = 2
class To_Do_List:
    def __init__(self, task_list = None):
        self.count = 0
        self.to_do = {}
        if task_list != None:
            for item in task_list:
                self.count += 1
                self.to_do[self.count] = [item,LOW]
                
        self.print_list()

    def print_list(self):
        print(" ")
        for num in self.to_do.keys():
            if self.to_do[num][1] == 0:
                priority = "low"
            elif self.to_do[num][1] == 1:
                priority = "Medium"
            else:
                priority = "High"
            line_to_print = "%i: '%s' Priority: %s" % (num,self.to_do[num][0],priority)
            print(line_to_print)
        print(" ")


#test_code
my_list = ["milk","pick up 4 kids", "call bobby"]
To_Do_List(my_list)
