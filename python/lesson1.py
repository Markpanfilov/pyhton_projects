#print(5)
#print(5+5)
#print("Hello World")
import random 
#input("Enter Nickname ")
secret_number=random.randint(1,100)
counter=5
while counter>0:
    our_number=input("enter number")
    our_number=int(our_number)
    if secret_number>our_number:
        print("secret number is bigger")
    if secret_number<our_number:
        print("secret number is smaller")
    if secret_number==our_number:
        print("you have guessed it!")
        break
    counter=counter-1
if counter==0:
    print ("GAME OVER")
    print("secret number was "+str (secret_number))
    
