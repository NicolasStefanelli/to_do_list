import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
from enum import Enum
LOW = 0
MED = 1
HI = 2

def Convert_Str_to_Int(string_to_convert):
    if string_to_convert == "Low":
        string_as_num = LOW
    elif string_to_convert == "Medium":
        string_as_num = MED
    else:
        string_as_num = HI
    
    return string_as_num
    
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
        
        self.view.set_add_task_button_handler(self.add_task_button_handler)
        self.view.set_HI_button_handler(self.HI_button_handler)
        self.view.set_MED_button_handler(self.MED_button_handler)
        self.view.set_LO_button_handler(self.LO_button_handler)
        self.view.set_Clear_button_handler(self.Clear_button_handler)
        self.view.set_show_all_button_handler(self.show_all_button_handler)
        # start app
        self.view.window.mainloop() 
    
    # control definitions
    
    def add_task_button_handler(self):
            #print("add task selected")
            #print("adding task...")
            item = self.view.new_entry_task.get()
            priority = Convert_Str_to_Int(self.view.combobox_val.get())
            task_added = self.model.add_task(item,priority)
            if task_added == True:
                self.view.update_to_do_listbox([item])
    
    def HI_button_handler(self):
        print("Show High Prioirty")
        self.view.to_do_listbox.delete(0, tk.END)
        self.view.update_to_do_listbox(self.model.show_HI_priority())

    
    def MED_button_handler(self):
        print("Show Medium Prioirty")
        self.view.to_do_listbox.delete(0, tk.END)
        self.view.update_to_do_listbox(self.model.show_MED_priority())
    
    def LO_button_handler(self):
        print("Show Low Prioirty")
        self.view.to_do_listbox.delete(0, tk.END)
        self.view.update_to_do_listbox(self.model.show_LO_priority())
    
    def show_all_button_handler(self):
        print("show all")
        self.view.to_do_listbox.delete(0, tk.END)
        print("empty list")
        full_list = self.model.show_all()
        print("full list acquired")
        self.view.update_to_do_listbox(full_list)

    def Clear_button_handler(self):
        print("Clear All")
        self.model.dict = {LOW:[],MED:[],HI:[]}
        self.model.front = None
        self.view.to_do_listbox.delete(0, tk.END)

            

    


class To_Do_ListView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To Do List") # Replace with actual name

        self.add_frame = ttk.LabelFrame(self.window,text="Add Task",width = 300,height=50)
        self.add_frame.grid(row = 1,column = 1,sticky = tk.W+tk.E+tk.N+tk.S)
        task_label = ttk.Label(self.add_frame,text = "New Task")
        task_label.grid(row=1,column=1)
        
        self.new_entry_task = ttk.Entry(self.add_frame,width = 40)
        self.new_entry_task.grid(row = 1,column=2,pady=3)

        priority_label = ttk.Label(self.add_frame,text = " Priority of New Task")
        priority_label.grid(row=2,column=1,pady=3)

        self.combobox_val = tk.StringVar()
        self.priority_combobox = ttk.Combobox(self.add_frame,height=4,textvariable=self.combobox_val)
        self.priority_combobox.grid(row = 2,column=2,pady=3)
        self.priority_combobox['values'] = ("Low","Medium","High")

        self.add_task_button = ttk.Button(self.add_frame,text="Add Task")
        self.add_task_button.grid(row = 2,column=3)

        self.List = ttk.LabelFrame(self.window,text="List",width=300,height=400)
        self.List.grid(row=1,column=2,sticky = tk.W+tk.E+tk.N+tk.S)
        to_do_listbox_label = tk.Label(self.List,text = "To Do")
        to_do_listbox_label.grid(row = 1,column = 1,sticky = tk.N + tk.W)
        self.to_do_listbox = tk.Listbox(self.List,)
        self.to_do_listbox.grid(row = 2,column = 1)

        completed_listbox_label = tk.Label(self.List,text = "Completed Tasks")
        completed_listbox_label.grid(row = 3,column = 1,sticky = tk.N + tk.W)
        completed_listbox = tk.Listbox(self.List)
        completed_listbox.grid(row = 4,column = 1)

        self.exit = ttk.Frame(self.window,width = 300,height = 100)
        self.exit.grid(row = 1,column = 3, sticky = tk.W+tk.E+tk.N+tk.S)
        exit_button = ttk.Button(self.exit,text="Exit", command=self.window.quit)
        exit_button.grid(row = 1,column=1, pady = 10, padx = 5)

        self.viewing_options = ttk.LabelFrame(self.window,text = "Viewing Options", width = 300, height = 50)
        self.viewing_options.grid(row=2,column=1,sticky= tk.W+tk.E+tk.N+tk.S)

        self.HI_button = ttk.Button(self.viewing_options,text="Show Only High Priority")
        self.HI_button.grid(row = 1,column=1,pady = 4)
        self.MED_button = ttk.Button(self.viewing_options,text="Show Only Medium Priority")
        self.MED_button.grid(row = 2,column=1, pady = 4)
        self.LO_button = ttk.Button(self.viewing_options,text="Show Only Low Priority")
        self.LO_button.grid(row = 3,column=1, pady = 4)
        self.show_all_button = ttk.Button(self.viewing_options,text="Show All Tasks")
        self.show_all_button.grid(row = 1,column=2, pady = 4)
        self.Clear_button = ttk.Button(self.viewing_options,text="Clear All")
        self.Clear_button.grid(row = 2,column=2, pady = 4)

        


    # assign commands from the Controller
    def set_add_task_button_handler(self,handler):
        self.add_task_button.configure(command=handler)
    
    def set_HI_button_handler(self,handler):
        self.HI_button.configure(command=handler)
    
    def set_MED_button_handler(self,handler):
        self.MED_button.configure(command=handler)
    
    def set_LO_button_handler(self,handler):
        self.LO_button.configure(command=handler)
    
    def set_Clear_button_handler(self,handler):
        self.Clear_button.configure(command=handler)
    
    def set_show_all_button_handler(self,handler):
        self.show_all_button.configure(command=handler)
    
    # updates listboxes
    def update_to_do_listbox(self,my_list):
        for item in my_list:
            self.to_do_listbox.insert(tk.END,item)
    
    


        
class To_Do_ListModel:
    def __init__(self,item = None, priority = LOW):
        self.dict = {LOW:[],MED:[],HI:[]}
        self.front = None
        self.count = 0
        if item != None:
            self.front = Node(item,priority)
            self.dict[priority].append(item)
            self.count = 1
    
    def show_all(self):
        item_list = []
        curr = self.front 
        while curr.next != None:
            priority_str = None
            if curr.priority == 0:
                priority_str = "low"
            elif curr.priority == 1:
                priority_str = "Medium"
            else:
                priority_str = "High"
            item_list.append(curr.item)
            print("%s , Priority: %s" % (curr.item,priority_str))
            curr = curr.next
        return item_list

    def add_task(self,item, priority = LOW):
        #print("New Task entry: %s" % (item))
        #print("Add Task Successful")
        if item != "":
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

            return True
        else:
            return False
        

        
    
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

    def show_LO_priority(self):
        return self.dict[LOW]



if __name__ == "__main__":
    app = To_Do_List()