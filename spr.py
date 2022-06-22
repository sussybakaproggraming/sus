import random
import time
def sus(die):
    spr = ['scissors', 'paper', 'rock']
     # chooses between spr 'scissors', 'paper', 'rock'
    spr2 = random.choice(spr)
    if spr2 == 'scissors' and die == 'paper':
        print(spr2)
        print(die)
        print('You Lose')
    
    elif spr2 == 'scissors' and die == 'rock':
        print(spr2)
        print(die)
        print('You Win')
    
    elif spr2 == 'rock' and die == 'paper':
        print(spr2)
        print(die)
        print('You Win')
    
    elif spr2 == 'rock' and die == 'scissors':
        print(spr2)
        print(die)
        print('You Lose')
        
    elif spr2 == 'paper' and die == 'scissors':
        print(spr2)
        print(die)
        print('You Win')
    
    elif spr2 == 'paper' and die == 'rock':
        print(spr2)
        print(die)
        print('You Lose')
    
    elif spr2 == 'paper' and die == 'paper':
        print(spr2)
        print(die)
        print('Tie')
    
    elif spr2 == 'scissors' and die == 'scissors':
        print(spr2)
        print(die)
        print('Tie')
        
    elif spr2 == 'rock' and die == 'rock':
        print(spr2)
        print(die)
        print('Tie')
    else:
        print('do not even try')
    
print(sus(input("choose between rock , paper, scissors: ")))
time.sleep(10)