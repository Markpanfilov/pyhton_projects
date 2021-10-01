"""
    Цель урока: создать консольную игру крестики-нолики
    + вспомнить команды из предыдущего урока
    + создать поле для игры (многомерный массив)
    + создать функцию для отрисовки игровой доски
    + организовать ввод хода по координатам поля
    + создать функцию проверки победителя
    + организовать вывод трех возможных состояний: побидили крестики или нолики, ничья 
    + запретить повторный ввод в поле
    + получить домашнее задание
"""

area=[
        ["*","*","*"],
        ["*","*","*"],
        ["*","*","*"]
    ]
def print_area () :
    for line in area:
        print (*line)
print_area()
def check_winner () :
    #x by horizontal
    if area [0][0]== "X" and area [0][1]=="X" and area [0][2] == "X":
        return "X"
    elif area [1][0]== "X" and area [1][1]=="X" and area [1][2] == "X":
        return "X"
    elif area [2][0]== "X" and area [2][1]=="X" and area [2][2] == "X":
        return "X"
     #O by horizontal
    if area [0][0]== "O" and area [0][1]=="O" and area [0][2] == "O":
        return "O"
    elif area [1][0]== "O" and area [1][1]=="O" and area [1][2] == "O":
        return "O"
    elif area [2][0]== "O" and area [2][1]=="O" and area [2][2] == "O":
        return "O"
     #x by vertical
    if area [0][0]== "X" and area [1][0]=="X" and area [2][0] == "X":
        return "X"
    elif area [0][1]== "X" and area [1][1]=="X" and area [2][1] == "X":
        return "X"
    elif area [0][2]== "X" and area [1][2]=="X" and area [2][2] == "X":
        return "X"
      #o by vertical
    if area [0][0]== "O" and area [1][0]=="O" and area [2][0] == "O":
        return "O"
    elif area [0][1]== "O" and area [1][1]=="O" and area [2][1] == "O":
        return "O"
    elif area [0][2]== "O" and area [1][2]=="O" and area [2][2] == "O":
        return "O"   
      #x by diagonal
    elif area [0][0]== "X" and area [1][1]=="X" and area [2][2] == "X":
        return "X"
    elif area [0][2]== "X" and area [1][1]=="X" and area [2][0] == "X":
        return "X"   
    #O by diagonal
    elif area [0][0]== "O" and area [1][1]=="O" and area [2][2] == "O":
        return "O"
    elif area [0][2]== "O" and area [1][1]=="O" and area [2][0] == "O":
        return "O"
    else:
        return False
    
for turn in range (1,10):
    turn_char = "X" if turn% 2 else "O"
    print ("number of the turn:",turn,"now coming:",turn_char)
    row= int (input("choose the row"))-1
    cell= int (input("choose the column"))-1
    if area [row][cell]=="*":
        area [row] [cell]= turn_char
        if check_winner()== "X":
            print ("X wins")
            break
        if check_winner() == "O":
            print ("O wins")
            break
    else:
        print ("cell already taken.you miss a turn.")
    print_area()
    if check_winner() == False and turn == 9:
        print ("DRAW no one won this match")


