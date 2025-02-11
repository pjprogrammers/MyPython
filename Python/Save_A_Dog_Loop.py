from tkinter import *
from tkinter import messagebox as mg
a = mg.askquestion(title="Notice!",message="There Is A Dog About To Die Of Starvation , Would you Like To Save It ?",icon='info')
if a=='yes':
    b = mg.askquestion(title="Notice!",message="Would You Like To Donate $5 To Feed It ?")
    if b=='yes':
        b1 = mg.showinfo(title="Thank You",message="Thank You For Your Donation")
    else:
        c = mg.askquestion(title="Notice!",message="Do You Want The Dog To Die ?")
        if c=='yes':
            c1 = mg.askokcancel(title="Warning",message="Your Actions Might Take Someone\'s Life .")
            if c1 == True:
                 c2 = mg.showinfo(title="Information",message="The Dog Has Died .\n\n        ૮₍ 𝁽ܫ𝁽 ₎ა")
                 c2_2 = mg.askquestion(title="",message="Do You Feel Happy Now ?")
                 c2_3 = mg.showwarning(title="",message="You Are Evil .")
                 c2_4 = mg.showerror(title="Notice",message="You Have Obtained Rewards For KILLING A DOG .")
                 c2_5 = mg.showinfo(title="Rewards",message="You Have Successfully Obtained A Seat In Hell .")
            else:
                 c3 = mg.askquestion(title="",message="Do You Want To Save The Dog ?")
        else:
             d = mg.askquestion(title="Notice",message="Then Do You Want To Donate $5 To Save It ?")
else:
    c = mg.askquestion(title="Notice!",message="Do You Want The Dog To Die ?")
    if c=='yes':
            c1 = mg.askokcancel(title="Warning",message="Your Actions Might Take Someone\'s Life .")
            if c1 == True:
                 c2 = mg.showinfo(title="Information",message="The Dog Has Died .\n\n        ૮₍ 𝁽ܫ𝁽 ₎ა")
                 c2_2 = mg.askquestion(title="",message="Do You Feel Happy Now ?")
                 c2_3 = mg.showwarning(title="",message="You Are Evil .")
                 c2_4 = mg.showerror(title="Notice",message="You Have Obtained Rewards For KILLING A DOG .")
                 c2_5 = mg.showinfo(title="Rewards",message="You Have Successfully Obtained A Seat In Hell .")
            else:
                c3 = mg.askquestion(title="",message="Do You Want To Save The Dog ?")
    else:
             d = mg.askquestion(title="Notice",message="Then Do You Want To Donate $5 To Save It ?")