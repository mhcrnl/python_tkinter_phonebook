#Import as tk requires prefix "tk."
import Tkinter as tk
#Import Tkinter is global import
import Tkinter
from Tkinter import *
from Tkinter import Label, Menu, Frame, Button, LEFT, TOP, X, FLAT, RAISED 

class PhoneBook(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        #<create the rest of your GUI here>
        parent.title("PhoneBook")
        parent.geometry("400x400+100+140")
        """
        self.toolbar = Toolbar(self)
        self.toolbar.pack(side="top", fill="x")
        """
        #Adaugarea meniu barului
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)

        helpAbout = Menu(menubar)
        helpAbout.add_command(label="About")
        menubar.add_cascade(label="Help", menu=helpAbout)
        """
        #adaugarea toolbarului
        self.toolBar = tk.Toplevel(self.parent, bd=1, relief=RAISED)
        self.btnExit = Button(self.toolBar, relief=FLAT, command=self.quit)
        self.btnExit.pack(side=LEFT, padx=2, pady=2)
        self.toolBar(side=TOP, fill=X)
        """
        Label(self.parent, text="Nume/Prenume: ").pack()
        entNumePrenume = Entry(self.parent).pack() 
        
        self.pack()

        

class Toolbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        #<create the rest of your GUI here>
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)


def main():
    root = tk.Tk()
    PhoneBook(root)
    root.mainloop()
    root.destroy()

if __name__ == "__main__":
    main()
