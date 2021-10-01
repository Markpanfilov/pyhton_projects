#Цель урока - научиться работать с файлами
# + Вспомнить пройденный материал, использовать код базового текстового редактора
# - Создать папку file, создать в ней файл writers.txt и наполнить его текстом
# - Создать функции для открытия и сохранения файла
# - Научиться использовать диалоговые окна
# - Назначить диалоговые окна на каждую команду (при необходимости)
# - Создать все необходимые функц


from tkinter import*
window=Tk()
window.geometry("500x500")
window.title ("Notes")
def new():
    print ("new")
def open_file():
    print ("new1")
def save():
    print ("new2")
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
