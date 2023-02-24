from tkinter import *
from tkinter import ttk	
from tkinter.font import Font
from datetime import date

class To_do:

	def __init__(self, frame_to_add_to, tab_name):
		#creating frame for listbox
		self.frame = Frame(frame_to_add_to)
		self.tab_name = tab_name
		self.font  = Font(size=24)
		self.entry = Entry(frame_to_add_to, font=("Havletica",24), width=30)
		self.y_scrollbar = Scrollbar(self.frame)
		self.button_frame = Frame(frame_to_add_to)
		self.listbox = Listbox(self.frame,
		        font=self.font,
		        bd=0, 
		        width=30, 
		        height=13, 
		        highlightthickness=0,
		        selectbackground="#f4f4f4")

		self.open_list()

		self.frame.pack(pady=10)
		self.listbox.pack(side=LEFT)
		self.y_scrollbar.pack(side=RIGHT)
		self.entry.pack(pady=5)
		self.button_frame.pack(pady=20)

		self.listbox.config(yscrollcommand=self.y_scrollbar.set)
		self.y_scrollbar.config(command=self.listbox.yview)


		
		# Add some buttons
		self.delete_button = Button(self.button_frame, text="Delete Item", 
									command=self.delete_item, font=("Havletica",24))
		self.add_button = Button(self.button_frame, text="Add Item", 
								command=self.add_item, font=("Havletica", 24))
		self.delete_button.grid(row=0, column=0)
		self.add_button.grid(row=0, column=1, padx=20)


	def delete_item(self):
		self.listbox.delete(ANCHOR)

	def add_item(self):
		if len(self.entry.get()) != 0:
			self.listbox.insert(END, self.entry.get())
		self.entry.delete(0, END)

	def save_list(self):
		stuff = self.listbox.get(0, END)	
		print(stuff)	
		with open('{}.txt'.format(self.tab_name), 'w') as f:
			for listitem in stuff:
				f.write('%s\n' % listitem)


	def open_list(self):
		with open('{}.txt'.format(self.tab_name), 'r') as f:
			stuff = f.readlines()
			for i in range(len(stuff)):
				stuff[i] = stuff[i][:-1]
		for item in stuff:
			self.listbox.insert(END, item)


def save():
    day_todo.save_list()	
    week_todo.save_list()	
    month_todo.save_list()	
    

root = Tk()
root.title("To-Do List")
root.geometry("500x600")
root.resizable(False, False)


#CREATING TABS AND GIVING THE A STYLE
style = ttk.Style()
style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0],  
        							"background": "#ffffff"},
        			  "map": {"background": [("selected", "#ffffff")]} 
        			  },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": "#ffffff" },
            "map":       {"background": [("selected", "#ffffff")],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("yummy")

#WORKING WITH NOTEBOOK TABS
note = ttk.Notebook(root)
f1 = Frame(note, width=500, height=600, bg="white")
note.add(f1, text = 'Day')
f2 = Frame(note, width=500, height=600, bg="white")
note.add(f2, text = 'Week')
f3 = Frame(note, width=500, height=600, bg="white")
note.add(f3, text = 'Month')
note.pack(expand=1, fill='both', padx=5, pady=5)

#FILLING UP THOSE TABS
day_todo = To_do(f1, "day")
week_todo = To_do(f2, "week")
month_todo = To_do(f3, "month")

#CREATING TOP MENU
menubar = Menu(root)
root.config(menu=menubar)
commands_menu = Menu(menubar)
menubar.add_cascade(label="Commands", menu=commands_menu)
commands_menu.add_command(label="Save", command=save)
root.mainloop()






