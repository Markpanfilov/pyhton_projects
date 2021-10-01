"""
  Цель урока + заложить основу для создания текстового редактора
   + Вспомнить пройденный материал
   + Определить из каких базовых компонентов состоит текстовый редактор
   + Подключить библиотеку интерфейсов, создать окно, установить размер окна и заголовок окна
   + Создать многострочное текстовое поле (обеспечить перенос по словам, растяжение по всему окну)
   + Создать главное меню, добавить меню файл с тремя командами (Новый, Открыть, Сохранить)
   + Добавить иконки для каждой команды
  + Получить домашнее задание
"""

from tkinter import*
import tkinter.filedialog
file_path=""
window=Tk()
window.geometry("500x500")
window.title ("Notes")
def new():
    global file_path
    txt.delete("1.0","end")
    file_path=""
def open_file():
    global file_path
    file_path=tkinter.filedialog.askopenfilename()
    with open(file_path) as file:
        txt.delete("1.0","end")
        txt.insert("1.0",file.read())
def save ():
    global file_path
    content= txt.get("1.0","end")
    if file_path=="":
        file_path=tkinter.filedialog.asksaveasfilename()                                                                                                                                                                                                                
        with open(file_path,"w") as file:
            file.write (content)
    else :
        with open(file_path,"w") as file:
            file.write (content)
def cut():
    txt.event_generate("<<Cut>>")
def copy():
    txt.event_generate("<<Copy>>")
def paste():
    txt.event_generate("<<Paste>>")
new_file_icon=PhotoImage(file="icons/new_file.gif")
open_file_icon=PhotoImage(file="icons/open_file.gif")
save_file_icon=PhotoImage(file="icons/save.gif")
cut_file_icon=PhotoImage(file="icons/cut.gif")
copy_file_icon=PhotoImage(file="icons/copy.gif")
paste_file_icon=PhotoImage(file="icons/paste.gif")
txt=Text(window,wrap="word")
txt.pack(expand="yes",fill="both")
menu_bar=Menu(window)
file_menu=Menu(menu_bar)
menu_bar.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New",image=new_file_icon,compound="left",command=new)
file_menu.add_command(label="Open",image=open_file_icon,compound="left",command=open_file)
file_menu.add_command(label="Save",image=save_file_icon,compound="left",command=save)
edit_menu=Menu(menu_bar)
menu_bar.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_command(label="cut",image=cut_file_icon,compound="left",command=cut)
edit_menu.add_command(label="copy",image=copy_file_icon,compound="left",command=copy)
edit_menu.add_command(label="paste",image=paste_file_icon,compound="left",command=paste)
window.config(menu=menu_bar)































window.mainloop()
