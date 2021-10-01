"""
    Цель урока: создать простейший калькулятор
    + вспомнить команды из предыдущего урока
    + познакомиться с графической библиотекой tkinter
    + создать первое окно с указанными размерами и заголовком
    + научиться создавать виджеты (объекты) в окне
    + научиться размещать виджеты на окне
    + познакомиться с функциями
    + создать калькулятор, который суммирует и вычитает два числа
    + получить домашнее задание
"""
from tkinter import *
window=Tk()

window.geometry("500x500")
window.title("CALCULATOR")
def add():
    n1=int( text_Nr1.get("1.0","end") )
    n2=int( text_Nr2.get("1.0","end") )
    ans=n1+n2
    text_Nra.delete("1.0","end")
    text_Nra.insert("1.0",ans)
def sub():
    n1=int( text_Nr1.get("1.0","end") )
    n2=int( text_Nr2.get("1.0","end") )
    ans=n1-n2
    text_Nra.delete("1.0","end")
    text_Nra.insert("1.0",ans)
def mult():
    n1=int( text_Nr1.get("1.0","end") )
    n2=int( text_Nr2.get("1.0","end") )
    ans=n1*n2
    text_Nra.delete("1.0","end")
    text_Nra.insert("1.0",ans)
def div():
    n1=int( text_Nr1.get("1.0","end") )
    n2=int( text_Nr2.get("1.0","end") )
    ans=n1/n2
    text_Nra.delete("1.0","end")
    text_Nra.insert("1.0",ans)
BUTTON_ADD=Button(window,text="+",command=add)
BUTTON_ADD.place(x=10,y=40)
button_mult=Button(window,text="*",command=mult)
button_mult.place(x=50,y=40)
button_div=Button(window,text="/",command=div)
button_div.place(x=70,y=40)
button_sub=Button(window,text="-",command=sub)
button_sub.place(x=30,y=40)
text_Nr1=Text(window,width=15,height=1)
text_Nr1.place(x=20,y=100)
text_Nr2=Text(window,width=15,height=1)
text_Nr2.place(x=20,y=136)
text_Nra=Text(window,width=15,height=1)
text_Nra.place(x=20,y=172)
window.mainloop()
