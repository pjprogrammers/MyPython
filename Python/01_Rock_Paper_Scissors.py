import random 

def play():
    user = input("What's Your Choice ? , 'r'for rock ,'p'for paper,'s'for scissors : ")
    global computer
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'
    
    # r>s , s>p , p>r
    if win(user,computer):
        return 'You Won !'
    
    return 'You Lost !'
    
def win(player,opponent):
    # return true if player wins
    # r>s , s>p , p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())
print(computer)