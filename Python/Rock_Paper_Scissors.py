import random
from tkinter import *
from tkinter import messagebox as mg


r = "Rock"
p = "Paper"
s = "Scissors"
def play(user):
    computer = random.choice([r,p,s])

    if user == computer:
        result = 'It\'s a tie'
    
    # r>s , s>p , p>r
    elif win(user,computer):
        result =  'You Won !'
     
    else:
        result =  'You Lost !'
    
    mg.showinfo(title ="Result",message= f"{result}\nThe Computer Chose: {computer}")

def win(player,opponent):
    # return true if player wins
    # r>s , s>p , p>r
    if (player == r and opponent == s) or (player == s and opponent == p) or (player == p and opponent == r):
        return True                        


#Setup The GUI
window = Tk()
window.title("Rock Paper Scissors")
window.geometry("400x300") #Window Size
window.config(bg="black")

label = Label(window,text="Choose One Of The Options")
label.config(font=("Monospace",13,"bold","underline"))
label.config(bg="black",fg="white")
label.pack(side=TOP,padx=0,pady=50)


#Create A Frame To Hold The Buttons
frame = Frame(window)
frame.config(bg="black")
frame.pack(side=TOP)

# Button Configuration
button_config = {
    'font': ('Helvetica', 15,'bold'),
    'fg': 'cyan',
    'bg': 'gray',
    'width': 7,
    'height': 2,
    'relief': 'raised',
    'bd': 10,
    'activebackground': 'silver',
    'activeforeground': 'cyan'
}

# Create Buttons
rock_button = Button(frame, text="Rock", command=lambda: play(r), **button_config)
paper_button = Button(frame, text="Paper", command=lambda: play(p), **button_config)
scissors_button = Button(frame, text="Scissors", command=lambda: play(s), **button_config)


# Position buttons in a 3-column grid
rock_button.grid(row=0, column=0, padx=7, pady=20)
paper_button.grid(row=0, column=1, padx=7, pady=20)
scissors_button.grid(row=0, column=2, padx=7, pady=20)


window.mainloop()
        
        