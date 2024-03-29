from Tkinter import *

#First create application class
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #These variables will be used in the poll function so i 
        #Set them at the start of the program to avoid errors.
        self.search_var = StringVar()
        self.switch = False
        self.search_mem = ''

        self.pack()
        self.create_widgets()

    #Create main GUI window
    def create_widgets(self):
        #Use the StringVar we set up in the __init__ function 
        #as the variable for the entry box
        self.entry = Entry(self, textvariable=self.search_var, width=13)
        self.lbox = Listbox(self, width=45, height=15)

        self.entry.grid(row=0, column=0, padx=10, pady=3)
        self.lbox.grid(row=1, column=0, padx=10, pady=3)
        
        #Function for updating the list/doing the search
        self.update_list()

        self.poll()

    #Runs every 50 milliseconds. 
    def poll(self):
        #Get value of the entry box
        self.search = self.search_var.get()
        if self.search != self.search_mem: #self.search_mem = '' at start of program.
            self.update_list(is_contact_search=True)

            #set switch and search memory
            self.switch = True #self.switch = False at start of program.
            self.search_mem = self.search

        #contact window events / return to '' after preforming search needs to
        #reset the contents of the list box. I use a 'switch' to determine when
        #it needs to be updated.
        if self.switch == True and self.search == '':
            self.update_list()
            self.switch = False
        self.after(50, self.poll)

    def update_list(self, **kwargs):
        try:
            is_contact_search = kwargs['is_contact_search']
        except:
            is_contact_search = False
        lbox_list = ['Adam', 'Lucy', 'Barry', 'Bob', 'James', 'Frank', 'Susan', 'Amanda', 'Christie']
        self.lbox.delete(0, END)
        for item in lbox_list:
            if is_contact_search == True:
                if self.search.lower() in item.lower():
                    self.lbox.insert(END, item)
            else:
                self.lbox.insert(END, item)

root = Tk()
root.title('Filter Listbox Test')
app = Application(master=root)
print 'Starting mainloop()'
app.mainloop()

