from tkinter import Tk, Label, Button

class Calculator():
    def __init__(self):
        self.root = Tk()
        root = self.root

        root.title('GPA Calculator')
        root.geometry('360x400')
        root.config()

        self.grade1 = Label(root)
        self.grade1.config(text='Class 1:')
        self.grade1.place(x=40, y=30)

        self.grade2 = Label(root)
        self.grade2.config(text='Class 2:')
        self.grade2.place(x=40, y=70)

        self.grade3 = Label(root)
        self.grade3.config(text='Class 3:')
        self.grade3.place(x=40, y=110)

        self.grade4 = Label(root)
        self.grade4.config(text='Class 4:')
        self.grade4.place(x=40, y=150)

        self.grade5 = Label(root)
        self.grade5.config(text='Class 5:')
        self.grade5.place(x=40, y=190)

        self.grade6 = Label(root)
        self.grade6.config(text='Class 6:')
        self.grade6.place(x=40, y=230)

        self.GPAlabel = Label(root)
        self.GPAlabel.config(text='Your GPA:')
        self.GPAlabel.place(x=40, y=330)

        self.calculate = Button(text='Calculate')
        self.calculate.place(x=120, y=270)
        self.calculate.config(foreground='black', background='gray', relief='sunken')
        self.calculate.config(height=2, width=10)

        self.grade_label = Label(root)
        self.grade_label.place(x=130, y=325)
        self.grade_label.config(bg='light gray')
        self.grade_label.config(height=2, width=8)
        self.grade_label.config(foreground='black')
