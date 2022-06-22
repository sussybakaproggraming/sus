import random
import time

spr = ['jesus christ you stupid', 
       'stupid idiot', 
       'dumb ass rock',
       'smoke weed everyday', 
       'stupid idiot', 
       'dumb ass rock',
       ' You’re the reason God created the middle finger'
       'I thought of you today. It reminded me to take out the trash',
       'OH MY GOD! IT SPEAKS!',
       'Mirrors can’t talk. Lucky for you, they can’t laugh, either.',
       'Grab a straw, because you suck',
       'You’re the reason the gene pool needs a lifeguard',
       'If I wanted to kill myself, I would climb to your ego and jump to your IQ',
       'Don’t be ashamed of who you are. That’s your parent’s job.',
       'If your brain was dynamite, there wouldn’t be enough to blow your hat off',
       'Unless your name is Google, stop acting like you know everything!',
       'dont you have some thing better to do like touching grass?'
       ]
spr2 = random.choice(spr)



inputone = int(input("1st Number: "))
inputtwo = input("Enter operator: ")
inputthree = int(input("2st Number: "))

if inputtwo == '+':
 time.sleep(3.0)   
 print("Computer is Calculating...")
 time.sleep(3.0)
 print(spr2)
 time.sleep(3.0)
 print(inputone + inputthree)

elif inputtwo == '-':
 time.sleep(3.0)   
 print("Computer is Calculating...")
 time.sleep(3.0)
 print(spr2)
 time.sleep(3.0)
 print(inputone - inputthree)
 
elif inputtwo == '/':
 time.sleep(3.0)   
 print("Computer is Calculating...")
 time.sleep(3.0)
 print(spr2)
 time.sleep(3.0)
 print(inputone / inputthree)
    

elif inputtwo == '*':
 time.sleep(3.0)   
 print("Computer is Calculating...")
 time.sleep(3.0)
 print(spr2)
 time.sleep(3.0)
 print(inputone * inputthree)
    
elif inputtwo == '**':
 time.sleep(3.0)   
 print("Computer is Calculating...")
 time.sleep(3.0)
 print(spr2)
 time.sleep(3.0)
 print(inputone ** inputthree)
 

else:
    print("you smell like cheese")

