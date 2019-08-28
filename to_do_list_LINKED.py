import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
from enum import Enum
LOW = 0
MED = 1
HI = 2

class Node:
    def __init__(self,item, priority = LOW, nextz = None):
        self.item = item
        self.priority = priority
        self.next = nextz

class To_Do_List:
    """This is the controller"""
    def __init__(self):
        """Initilizes the app"""
    
        # create model
        self.model = To_Do_ListModel()

        # create view
        self.view = To_Do_ListView()

        # create controls
        self.view.set_new_entry_task_handler(self.new_entry_task_handler)
        self.view.priority_combobox
        self.view.set_add_task_button_handler(self.add_task_button_handler)

        # start app
        self.view.window.mainloop() 
    
    # control definitions

    def add_task_button_handler(self):
            print("add task")

    


class To_Do_ListView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To Do List") # Replace with actual name

        self.add_frame = ttk.LabelFrame(self.window,text="Add Task",width = 300,height=50)
        self.add_frame.grid(row = 1,column = 1,sticky = tk.W+tk.E+tk.N+tk.S)
        task_label = ttk.Label(self.add_frame,text = "New Task")
        task_label.grid(row=1,column=1)
        
        new_entry_task = ttk.Entry(self.add_frame,width = 40)
        new_entry_task.grid(row = 1,column=2,pady=3)

        priority_label = ttk.Label(self.add_frame,text = " Priority of New Task")
        priority_label.grid(row=2,column=1,pady=3)

        self.combobox_val = tk.StringVar()
        priority_combobox = ttk.Combobox(self.add_frame,height=4,textvariable=self.combobox_val)
        priority_combobox.grid(row = 2,column=2,pady=3)
        priority_combobox['values'] = ("Low","Medium","High")

        self.add_task_button = ttk.Button(self.add_frame,text="Add Task")
        self.add_task_button.grid(row = 2,column=3)

        self.viewing_options = ttk.LabelFrame(self.window,text = "Viewing Options", width = 300, height = 50)
        self.viewing_options.grid(row=2,column=1,sticky= tk.W+tk.E+tk.N+tk.S)

        HI_button = ttk.Button(self.viewing_options,text="Show Only High Priority")
        HI_button.grid(row = 1,column=1,pady = 4)
        MED_button = ttk.Button(self.viewing_options,text="Show Only Medium Priority")
        MED_button.grid(row = 2,column=1, pady = 4)
        LO_button = ttk.Button(self.viewing_options,text="Show Only Low Priority")
        LO_button.grid(row = 3,column=1, pady = 4)
        Clear_button = ttk.Button(self.viewing_options,text="Clear All")
        Clear_button.grid(row = 1,column=2, pady = 4)

        self.List = ttk.LabelFrame(self.window,text="List",width=300,height=400)
        self.List.grid(row=1,column=2,sticky = tk.W+tk.E+tk.N+tk.S)
        to_do_listbox_label = tk.Label(self.List,text = "To Do")
        to_do_listbox_label.grid(row = 1,column = 1,sticky = tk.N + tk.W)
        to_do_listbox = tk.Listbox(self.List,)
        to_do_listbox.grid(row = 2,column = 1)

        completed_listbox_label = tk.Label(self.List,text = "Completed Tasks")
        completed_listbox_label.grid(row = 3,column = 1,sticky = tk.N + tk.W)
        completed_listbox = tk.Listbox(self.List)
        completed_listbox.grid(row = 4,column = 1)

        self.exit = ttk.Frame(self.window,width = 300,height = 100)
        self.exit.grid(row = 1,column = 3, sticky = tk.W+tk.E+tk.N+tk.S)
        exit_button = ttk.Button(self.exit,text="Exit", command=self.window.quit)
        exit_button.grid(row = 1,column=1, pady = 10, padx = 5)

    # assign commands from the Controller
        
    def set_add_task_button_handler(self,handler):
        self.add_task_button.configure(command=handler)
    
    def 


        
class To_Do_ListModel:
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
            if curr.priority == 0:
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

        while found != True:
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



if __name__ == "__main__":
    app = To_Do_List()