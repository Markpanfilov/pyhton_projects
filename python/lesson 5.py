"""Цель урока - научиться работать с файлами+ Вспомнить пройденный материал- Создать папку file, создать в ней файл words.txt и наполнить его текстом- Научиться открывать, читать и закрывать файл- Создать пустой файл blank.txt в папке file- Научиться записывать новую информацию в файл- Научиться использовать конструкцию with .. as:- Научиться добавлять новую информацию в файл- Получить домашнее задание"""file1=open("files/data1.txt","a")file=open("files/words.txt")for line in file:    file1.write (line)file.close()file1.close()file=open("files/data.txt","a")file.write ("hello \n")file.close()