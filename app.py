import random
possible=['rock','paper','scissors']
while True:
    user=input('\nEnter a your choice:rock, paper or scissors? ')
    while user not in possible:
        print('Not a valid choice,enter a valid choice!')
        user=input('\nEnter a your choice:rock, paper or scissors? ')
    compchoice=random.choice(possible)
    print('you chose',user,'computer chose',compchoice)
    if user==compchoice:
        print('both chose',user,'its a tie')
    elif user=='rock':
        if compchoice=='paper':
            print('paper crumples rock,you lose')
        elif compchoice == 'scissors':
            print('rock crumples scissors,you win')
    elif user=='paper':
        if compchoice=='rock':
            print('paper crumples rock,you win')
        elif compchoice == 'scissors':
            print('scissors cuts paper,you lose')
    elif user=='scissors':
        if compchoice=='rock':
            print('rock crumples scissors,you lose')
        elif compchoice == 'paper':
            print('scissors cuts paper,you win')
    play=input('wanna play again?y/n: ')
    while play not in ['y','n']:
        print('invalid choice type again')
        play=input('wanna play again?y/n: ')
    if play!='y':
      break
            
            
        
            
                    
            