"""
	Цель урока: создать консольную игру  "поле чудес"
	+ вспомнить команды из предыдущего урока
	+ изучить списки (массивы)
	+ познакомиться с циклом for
	+ познакомиться с командой len
	+ познакомиться с командой "in" и "not in"
	+ познакомиться с параметром end для команды print
	+ на основе новых и старых команд создать игру "поле чудес"
	+ получить домашнее задание
"""


word="Hello"
a=3
letters=[]
while a>0:
    if len (word)==len (letters):
        print ("YOU WIN")
        break
    letter=input ("enter letter")
    if letter in letters:
        a-=1
        print ("double entry is forbidden, you have",a,"lives left")
    else:
        letters.append(letter)
    for c in word:
        if c in letters:
            print (c,end=" ")
        else :
            print ("*", end=" ")
    if letter not in word:
        a-=1
        letters.pop()
        print("incorrect,you have",a,"lives left")
    if a==0:
        print ("YOU LOSE")

       

            
