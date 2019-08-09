LOW = 0
MED = 1
HI = 2

class Node:
    def __init__(self,item, priority = LOW, nextz = None):
        self.item = item
        self.priority = priority
        self.next = nextz

class To_Do_List:
    def __init__(self,item = None, priority = LOW):
        self.dict = {LOW:[],MED:[],HI:[]}
        self.front = None
        self.count = 0
        if item != None:
            self.front = Node(item,priority)
            self.dict[priority].append(item)
            self.count = 1
    
    def print_list(self):
        curr = self.front 
        while curr.next != None:
            priority_str = None
             if curr..priority == 0:
                priority_str = "low"
            elif curr.prioirty == 1:
                priority_str = "Medium"
            else:
                priority_str = "High"
            print("%s , Priority: %s" % (curr.item,priority_str))
            curr = curr.next
        print(curr.item)

    def add_item(self,item, priority = LOW):
        curr = self.front
        if self.front == None:
            self.front = Node(item,priority)
            self.dict[priority].append(item)
            self.count += 1
        else:
            curr = self.front
            while curr.next != None:
                curr = curr.next
            curr.next = Node(item,priority)
            self.dict[priority].append(item)
            self.count += 1


        
    
    def remove_item(self,item):
        if self.front.item == item:
            self.dict[self.front.priority].remove(item)
            self.front = self.front.next
        else:
            curr = self.front
            while curr.next.item != item:
                curr = curr.next
            curr.next = curr.next.next
            self.dict[self.front.priority].remove(item)


    def display_priority(self,item):
        found = False
        curr = self.front

        while found not True:
            if curr.item == item:
                found = True
            else:
                curr = curr.next

        return curr.priority


    def show_HI_priority(self):
        return self.dict[HI]

    def show_MED_priority(self):
        return self.dict[MED]

    def show_LOW_priority(self):
        return self.dict[LOW]

