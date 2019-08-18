from tkinter import *
import random
from tkinter import filedialog as fd

class Application(Frame):
    """ The simple apllication with GUI"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Creating a grid
        for i in range(17):
            for j in range(8):
                self.l = Label(root, text='Label %d.%d' % (i, j), relief=RIDGE)
                self.l.grid(row=i, column=j, sticky=NSEW)

        """Creating widgets"""

        #Menu
        self.menu = Menu(self)
        self.submenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.submenu)
        self.submenu.add_command(label="Open", command=self.open_file)
        self.submenu.add_command(label="Save", command=self.save_file)
        root.config(menu=self.menu)

        #Empty label
        self.lb1=Label(root, bg='#D9D9F3')
        self.lb1.grid(row=0, rowspan=17, column=0, columnspan=8, sticky=NSEW)

        #Label for Entry
        self.lb2=Label(root, bg='#D9D9F3', font = ("Verdana", 11), text='Input your list')
        self.lb2.grid(row=1,column=0,columnspan=3, rowspan=2,sticky=N+EW)
        self.lb3=Label(root, bg='#D9D9F3', font = ("Verdana", 9), text='One line = one element')
        self.lb3.grid(row=1,column=0,columnspan=3, rowspan=2,sticky=S)

        #Entry
        self.ent1=Entry(root)
        self.textvar = StringVar()
        self.ent1.config(textvariable=self.textvar, foreground = 'gray')
        self.textvar.set('You can clear the entry by LMB')
        self.ent1.grid(row=1, column=3, columnspan=4, rowspan=2,sticky=NSEW)
        self.ent1.bind('<Return>', self.reveal) # Event handler for Enter

        #Button 'Accept'
        self.submit_bttn = Button(root, text = "Accept", command = self.reveal)
        self.submit_bttn.grid(row = 4, column = 1, columnspan = 2, sticky = NSEW)

        #Button 'Draw'
        self.draw_bttn = Button(root, text = "Draw", command = self.draw)
        self.draw_bttn.grid(row = 4, column = 3, columnspan = 2, sticky = NSEW)

        #Button 'Reset'
        self.reset_bttn = Button(root, text = "Reset", command = self.reset)
        self.reset_bttn.grid(row = 4, column = 5, columnspan = 2, sticky = NSEW)

        #Label for Textbox1
        self.txt_label1=Label(root, bg='silver', text = 'Entered list: ')
        self.txt_label1.grid(row=5, column=0, columnspan=8, sticky=NSEW)

        #Textbox 1
        self.list_txt = Text(root, width = 35, height = 5, wrap = WORD)
        self.sb_textbox = Scrollbar(self.list_txt)
        self.list_txt.config(yscrollcommand = self.sb_textbox.set)
        self.list_txt.grid(row=6, column=0, rowspan=6, columnspan=8, sticky= NSEW)
        self.sb_textbox.config(command=self.list_txt.yview)
        self.sb_textbox.place(in_= self.list_txt, height = 123, x=443)

        #Label for Textbox2
        self.txt_label2 = Label(root, bg='silver', text= "Chosen element: ")
        self.txt_label2.grid(row=12, column=0, columnspan=8, sticky=NSEW)

        #Textbox 1
        self.chosen_txt = Text(root, width = 35, height = 5, wrap = WORD)
        self.chosen_txt.grid(row=13, column=0, rowspan=2, columnspan=8, sticky= NSEW)

        #Empty Label
        self.txt_label2 = Label(root, bg='#D9D9F3')
        self.txt_label2.grid(row=15, column=0, rowspan=2, columnspan=8, sticky=NSEW)

        #Signature
        self.txt_label2 = Label(root, bg='#D9D9F3', text= "Created by Emilia")
        self.txt_label2.grid(row=16, column=6, columnspan=2, sticky=W)

    def reveal(self,*event):
        """ Displaying entered text in Textbox1"""
        global list1
        contents = self.ent1.get()
        list1.append(contents)
        message='\n'.join(list1)

        self.list_txt.delete(0.0, END)
        self.ent1.delete(0, END)  # Clear Entry
        self.list_txt.insert(0.0, message)



    def draw(self):
        """Drawing an element"""
        message1 = "The winner is: "+drawing(list1)

        self.chosen_txt.delete(0.0, END)
        self.chosen_txt.insert(0.0, message1)


    def open_file(self):
        """Opening a file .txt"""
        global list1
        filename = fd.askopenfilename(filetypes=[("Text", "*.txt")])
        if filename:
            with open(filename, "r", -1, "utf-8") as file:
                self.list_txt.delete(1.0, END)
                self.list_txt.insert(END, file.read())

            with open(filename, "r", -1, "utf-8") as file:
                for linia in file:
                    list1.append(linia.rstrip())

    def save_file(self):
        """Saving the content of list_txt to .txt"""
        # Calling SaveAs Dialog
        filename = fd.asksaveasfilename(filetypes=[('Text','.txt')],
                                        defaultextension="*.txt")

        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(self.list_txt.get(1.0, END))

    def reset(self):
        global list1
        """Clearing text boxes and the list"""
        self.list_txt.delete(0.0, END)
        self.chosen_txt.delete(0.0, END)
        list1=[]

    def clear_ent(self, event):
        """Clearing ent1 when LMB is used"""
        self.ent1.delete(0, END) # Clear Entry
        self.ent1.focus_set() #Set the focus back at the begining of the text field
        self.ent1.config(foreground='black')

    def mouse_event(self,event):
        """It clears ent1 at the first click by RMB and it also changes colour of font for ent1"""
        global click_count
        if click_count == 0:
            self.ent1.delete(0, END)
            self.ent1.config(foreground='black')
            self.ent1.focus_set()
            click_count +=1


def drawing(some_list):
    """Random drawing one item from the entered list"""
    try:
        global list1
        list1=tuple(list1)
        list2=list(list1)
        new_list=[]

        while len(list2) != 0:
            chosen=random.choice(list2)
            new_list.append(chosen)
            list2.remove(chosen)

        return random.choice(new_list) # generating a random by a second time

    except IndexError:
        return "The list is empty"

list1=[]

# Main
root = Tk()
root.title("Lottery machine")
root.resizable(width=False, height=False)

app = Application(root)
root.bind_class('Entry', '<Button-3>', app.clear_ent)
click_count = 0
app.ent1.bind('<Button-1>', app.mouse_event)

root.mainloop()
