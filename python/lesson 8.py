"""Цель урока: создать игру крестики-нолики с интерфейсом- вспомнить команды из предыдущего урока- подключить библиотеку для создания интерфейсов и системных сообщений- создать окно, установить размеры, заголовок и отключить растягивание- создать поле для игры (многомерный массив)- наполнить массив объектами кнопок- создать функцию для совершения хода по нажатию кнопки- создать функцию по очистке игрового поля- создать функцию проверки победителя- организовать вывод трех возможных состояний: побидили крестики или нолики, ничья - запретить повторный ввод в поле- получить домашнее задание"""from tkinter import *from tkinter import messageboxwindow=Tk()window.geometry("600x600")window.resizable(False,False)area=[]turn=1def check_winner () :    #x by horizontal    if area [0][0]["text"]== "X" and area [0][1]["text"]=="X" and area [0][2]["text"]== "X":        return "X"    elif area [1][0]["text"]== "X" and area [1][1]["text"]=="X" and area [1][2]["text"]== "X":        return "X"    elif area [2][0]["text"]== "X" and area [2][1]["text"]=="X" and area [2][2]["text"]== "X":        return "X"     #O by horizontal    if area [0][0]["text"]== "O" and area [0][1]["text"]=="O" and area [0][2]["text"]== "O":        return "O"    elif area [1][0]["text"]== "O" and area [1][1]["text"]=="O" and area [1][2]["text"]== "O":        return "O"    elif area [2][0]["text"]== "O" and area [2][1]["text"]=="O" and area [2][2]["text"]== "O":        return "O"     #x by vertical    if area [0][0]["text"]== "X" and area [1][0]["text"]=="X" and area [2][0]["text"]== "X":        return "X"    elif area [0][1]["text"]== "X" and area [1][1]["text"]=="X" and area [2][1]["text"]== "X":        return "X"    elif area [0][2]["text"]== "X" and area [1][2]["text"]=="X" and area [2][2]["text"]== "X":        return "X"      #o by vertical    if area [0][0]["text"]== "O" and area [1][0]["text"]=="O" and area [2][0]["text"]== "O":        return "O"    elif area [0][1]["text"]== "O" and area [1][1]["text"]=="O" and area [2][1]["text"]== "O":        return "O"    elif area [0][2]["text"]== "O" and area [1][2]["text"]=="O" and area [2][2]["text"]== "O":        return "O"         #x by diagonal    elif area [0][0]["text"]== "X" and area [1][1]["text"]=="X" and area [2][2]["text"]== "X":        return "X"    elif area [0][2]["text"]== "X" and area [1][1]["text"]=="X" and area [2][0]["text"]== "X":        return "X"       #O by diagonal    elif area [0][0]["text"]== "O" and area [1][1]["text"]=="O" and area [2][2]["text"]== "O":        return "O"    elif area [0][2]["text"]== "O" and area [1][1]["text"]=="O" and area [2][0]["text"]== "O":        return "O"    else:        return Falsedef clear():    global turn,area    turn=1    for row in range (3):       for column in range (3):           area [row][column]["text"]=""def pushbutton (obj):    global turn    if not turn%2:        char= "O"    else:        char="X"    if obj ["text"]=="":        obj ["text"]=char        turn+=1        if check_winner()=="X":            print ("X")            messagebox.showinfo(title="winner",message="X")            clear()        if check_winner()=="O":            print ("O")            messagebox.showinfo(title="winner",message="O")             clear()        if check_winner()==False and turn==10:            print ("draw")            messagebox.showinfo(title="result",message="draw")            clear()for row in range (0,3):    area.append([])    for column in range (0,3):        area[row].append(Button(window,width=27,height=13))        area[row][column].grid(row=row ,column=column)        area[row][column]["command"]=lambda obj= area[row][column]:pushbutton (obj)           window.mainloop()