"""
	Цель урока: научиться использовать Canvas в tkinter
	-	Вспомнить команды длы работы с tkinter
	-	Подключить библиотеки: случайных чисел, интерфейса (создать окно 700x800)
	-	Создать массив цветов
	-	Создать холст на форме
	-	Создать класс для рисования разнацветных кругов в случайном положении
	-	Создать кнопку для вызова функции рисующей круги
	-	Создать класс для отрисовки квадрата шахматной доски
	-	Создать функцию рисующую шахматное поле
	- 	Домашнее задание: создать кнопку рисующую домики.
"""
from tkinter import*
from random import*
window=Tk()
window.geometry("700x700")
window.resizable(False,False)
window.title("~paint~")
size=600
canvas=Canvas(window,width=size,height=size)
canvas.grid(row=1,column=0,columnspan=3)
class Circle:
    name=""
    def __init__(self,tag):
        self.colours=["red","green","yellow","magenta","purple","pink","blue"]
        self.x=randint(10,450)
        self.y=randint(10,450)
        self.r=randint(33,200)
        self.tag=str(tag)
        self.colour=choice(self.colours)        
        canvas.create_oval(self.x,self.y,self.x+self.r,self.y+self.r,tag=self.tag,fill=self.colour)
        canvas.create_rectangle(self.x,self.y,self.x+self.r,self.y+self.r,outline="red")
    def update(self,pos):
        if Circle.name==""  and  pos[0]>self.x and pos[0]<self.x+self.r and pos[1]>self.y and pos[1]<self.y+self.r:
            Circle.name=self.tag
            self.x=pos[0] - self.r // 2
            self.y=pos[1] - self.r // 2
            canvas.create_oval(self.x,self.y,self.x+self.r,self.y+self.r,tag=self.tag,fill=self.colour)
            return int(self.tag)
        canvas.create_oval(self.x,self.y,self.x+self.r,self.y+self.r,tag=self.tag,fill=self.colour)
        return 0
class Square:
    def __init__(self,x,y,size,colour):
        self.x=x
        self.y=y
        self.size=size
        self.colour=colour
        canvas.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.colour)
class house:
    
    def __init__(self, x,y,size):
        self.x = x
        self.y = y
        self.size = size

def clickdown(event):
    
    canvas.delete("all")
    pos=(event.x,event.y)
    for circle in circles:
        i=circle.update(pos)
    circles[0],circles[i]=circles[i],circles[0]
    Circle.name=""
circles=[]
squares=[]
def chessboard():
    colours=["white","black"]
    change_size= size-20
    square_size=change_size//8
    colour_number=1
    i=65
    canvas.create_rectangle(0,0,size,size,outline="white",width=20)
    for row in range(10,change_size,square_size):
        canvas.create_text(row+square_size//2,6,text=chr(i),font="Calibri 8")
        canvas.create_text(row+square_size//2,size-4,text=chr(i),font="Calibri 8")
        i+=1
        j=1
        colour_number+=1
        for column in range (10,change_size,square_size):
            canvas.create_text(6,column+square_size//2,text=str(j),font="arial 9")
            canvas.create_text(size-4,column+square_size//2,text=str(j),font="arial 9")
            squares.append(Square(column,row,square_size,colours[colour_number%2]))
            colour_number+=1
            j+=1
def drawcircle():
    for i in range(1):
        circles.append(Circle(len(circles)))
button1=Button(window,text="draw a circle",command=drawcircle)
button1.grid(row=0,column=0)
button2=Button(window,text="draw a chess board",command=chessboard)
button2.grid(row=0,column=1)
button3=Button(window,text="draw a house")
button3.grid(row=0,column=2)
canvas.bind("<B1-Motion>",clickdown)
































































































window.mainloop()
