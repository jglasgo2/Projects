from tkinter import OptionMenu, Button, Label, Frame, StringVar
from gui import Calculator

class MainWindow(Calculator):
    def __init__(self, *args):
        Calculator.__init__(self)
        root = self.root

        #dictionary used to assign a numerical value to a letter
        grades = {
            "A": 4.0,
            "A-": 3.7,
            "B+": 3.3,
            "B": 3.0,
            "B-": 2.7,
            "C+": 2.3,
            "C": 2.0,
            "C-": 1.7,
            "D+": 1.3,
            "D": 1.0,
            "D-": 0.7,
            "F": 0.0
        }

        #list only used for dropdown menu
        options = [
            "A",
            "A-",
            "B+",
            "B",
            "B-",
            "C+",
            "C",
            "C-",
            "D+",
            "D",
            "D-",
            "F"
        ]

        #default values for grades
        default1 = StringVar()
        default1.set(' ')

        default2 = StringVar()
        default2.set(' ')

        default3 = StringVar()
        default3.set(' ')

        default4 = StringVar()
        default4.set(' ')

        default5 = StringVar()
        default5.set(' ')

        default6 = StringVar()
        default6.set(' ')

        #dropdown menus formatting
        self.grade_menu1 = OptionMenu(root, default1, *options)
        self.grade_menu1.place(x=150, y=30)
        self.grade_menu1.config(height=1, width=5)
        self.grade_menu1.config(bg='light gray')

        self.grade_menu2 = OptionMenu(root, default2, *options)
        self.grade_menu2.place(x=150, y=70)
        self.grade_menu2.config(height=1, width=5)
        self.grade_menu2.config(bg='light gray')

        self.grade_menu3 = OptionMenu(root, default3, *options)
        self.grade_menu3.place(x=150, y=110)
        self.grade_menu3.config(height=1, width=5)
        self.grade_menu3.config(bg='light gray')

        self.grade_menu4 = OptionMenu(root, default4, *options)
        self.grade_menu4.place(x=150, y=150)
        self.grade_menu4.config(height=1, width=5)
        self.grade_menu4.config(bg='light gray')

        self.grade_menu5 = OptionMenu(root, default5, *options)
        self.grade_menu5.place(x=150, y=190)
        self.grade_menu5.config(height=1, width=5)
        self.grade_menu5.config(bg='light gray')

        self.grade_menu6 = OptionMenu(root, default6, *options)
        self.grade_menu6.place(x=150, y=230)
        self.grade_menu6.config(height=1, width=5)
        self.grade_menu6.config(bg='light gray')


        def calculate():
            #using a list to get all the values at once
            letters = [
                default1.get(), 
                default2.get(), 
                default3.get(), 
                default4.get(), 
                default5.get(), 
                default6.get()
            ]

            denominator = 0.0
            numerator = 0.0

            for l in letters:
                if ' ' != l:
                    denominator += 1    
                for key, value in grades.items():
                    if l == key:
                        numerator += value
            
            if denominator == 0.0:
                self.grade_label.config(text='{:.2f}'.format(denominator))
            else:
                avg = numerator/denominator
                self.grade_label.config(text='{:.2f}'.format(avg))


        #mapping to calculate button
        self.calculate.config(command=calculate)
    
if __name__ in '__main__':
    window = MainWindow(Calculator)
    window.root.mainloop()
