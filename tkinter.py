import tkinter as tk 
from tkinter import messagebox
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("check button")
        self.root.geometry('500x500')
        self.label = tk.Label(self.root, text="Your Message", font=('Arial',18))
        self.label.pack(padx=10, pady=10)
        self.textBox = tk.Text(self.root, height=3, font=('Arial', 18))
        self.textBox.pack(padx=10,pady=10)
        self.button = tk.Button(self.root, text="schow message", font=('Arial',18),command=self.show_message)
        self.button.pack(padx=10,pady=10)
        self.checkstatus = tk.IntVar()
        self.checkbutton = tk.Checkbutton(self.root, text="schow Messagebox", font=('Arial',16), variable=self.checkstatus)
        self.checkbutton.pack(padx=10,pady=10)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close without asking", command=exit)
        self.filemenu.add_separator() # add the line between the commands
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu=self.menubar)
        self.buttonclear = tk.Button(self.root , text="clear", font=('Arial', 18), command=self.clear)
        self.buttonclear.pack(padx=20,pady=20)
        self.root.mainloop()
    def show_message(self):
        if self.checkstatus.get()== 0:
            print("cool, you passed")
        else:
            messagebox.showinfo(title='Message', message="you shoud to not choose the check Box")
    def on_closing(self):
        if messagebox.askyesno(title="Close", message="do you really want to close this window?"):
            self.root.destroy()
    def clear(self):
            self.textBox.delete('1.0', tk.END)
MyGUI()