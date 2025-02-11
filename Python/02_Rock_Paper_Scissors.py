import random 

r = "Rock"
p = "Paper"
s = "Scissors"
def play():
    user = input(''' What's Your Choice ?
'r'for rock ,'p'for paper,'s'for scissors : ''')
    global computer
    computer = random.choice([r,p,s])

    if tie(user,computer):
        return 'It\'s a tie'
    
    # r>s , s>p , p>r
    if win(user,computer):
        return 'You Won !'
    
    # r>s , s>p , p>r
    if lost(user,computer):
        return 'You Lost !'

def tie(player,opponent):
    # return true if it's a tie
    # r>s , s>p , p>r
    if (player == 'r' and opponent == r) or (player == 'p' and opponent == p) or (player == 's' and opponent == s):
        return True
    
def win(player,opponent):
    # return true if player wins
    # r>s , s>p , p>r
    if (player == 'r' and opponent == s) or (player == 's' and opponent == p) or (player == 'p' and opponent == r):
        return True
    
def lost(player,opponent):
    # return true if player wins
    # r>s , s>p , p>r
    if (player == 's' and opponent == r) or (player == 'p' and opponent == s) or (player == 'r' and opponent == p):
        return True
    
print(play())
print(f"The Computer Chose '{computer}'")