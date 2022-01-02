import random
def play():
    user = input("Enter your choice: r FOR ROCK, p FOR PAPER,s FOR SCISSIOR \n")
    computer= random.choice(['s','p','s'])
    a={
        's':"Scissor",
        'p':"Paper",
        "r":'Rock'
    }
    if user == computer:
        print("\n It's a tie...")
        return("")
    if is_win(user,computer):
        print("\n You won, Computor chose " + a[computer] )
        return("")
    else:
        print("You Lose, computor chose s"+ a[computer]) 
        return("")    

def is_win(player, opp):
    if(player == 'r' and opp == 's') or(player == 's' and opp=='p') or (player == 'p' and opp =='r'):
       return True

print(play())
