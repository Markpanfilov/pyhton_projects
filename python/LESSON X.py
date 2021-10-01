"""
	Цель урока: изучить классы и наследование
	+ разобрать простое создание класса и его методов
	+ научиться инициализировать класс и ссылаться на свой экземпляр
	+ изучить как реализуется наследование в классах
	+ получить домашнее задание
"""
class Transport:
    def __init__(self,wheels,fuel,driver):
        self.wheels=wheels
        self.fuel=fuel
        self.driver=driver
    def showinfo(self):
        print("i have",self.wheels,"wheels and i use",self.fuel,". my driver is ",self.driver)
class Car(Transport):
    def __init__(self,colour,wheels,fuel,driver):
        Transport.__init__(self,wheels,fuel,driver)
        self.colour=colour
    def say_colour(self):
        print("my colour is",self.colour)
        

BMW=Car("black",4,"petrol","Bob")
TESLA=Car("dark green",4,"electricity","alan_musk")

class Tank(Transport):
    def __init__(self,colour,wheels,fuel,driver):
        Transport.__init__(self,wheels,fuel,driver)
        self.colour=colour
    def say_colour(self):
        print("my colour is",self.colour)
    def showinfo(self):
        print("i have traks and i use",self.fuel,". my driver is ",self.driver)


MK11=Tank("green","","disel","someone who stole a tank")































































































































































































































































