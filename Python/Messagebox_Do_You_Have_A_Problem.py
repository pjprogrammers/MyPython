from tkinter import messagebox as mg
a = mg.askquestion(title="Question",message="Do You Have A Problem ?")
if a == "yes":
    b = mg.askquestion(title="Question",message="Can You Solve It ?")
    if b == "yes":
        c = mg.showinfo(title="Information",message="Then Why Worry ?")
    else:
        c = mg.showinfo(title="Information",message="Then Why Worry ?")
else:
    c = mg.showinfo(title="Information",message="Then Why Worry ?")       