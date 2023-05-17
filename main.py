def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} сейчас открыт!")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def show_spisok(self):
            for flavor in self.flavors:
                print(flavor)

    IceCream_Stand = IceCreamStand("BaskinRobbins", "Мороженое", ['Шоколадное', 'Клубничное', 'Ванильное', 'Мятное'])
    IceCream_Stand.show_spisok()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} сейчас открыт!")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, hours):
            self.flavors = flavors
            self.location = location
            self.hours = hours

        def show_spisok(self):
            print("Список сортов:")
            for flavor in self.flavors:
                print(flavor)

        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f"{flavor} добавлен в список сортов!")

        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} удалено из списка сортов!")
            else:
                print(f"{flavor} нет в списке сортов!")

        def proverka_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"{flavor} в наличии!")
            else:
                print(f"{flavor} нет в наличии!")

    newIceCreamStand = IceCreamStand("Мороженое", "Кафе маороженое",["Фруктовое","Клубничное","Шоколадное"],"улица Пушкина 3","0:00-6:00")

    newIceCreamStand.show_spisok()
    newIceCreamStand.add_flavor("Пломбир")
    newIceCreamStand.show_spisok()
    newIceCreamStand.remove_flavor("Фруктовое")
    newIceCreamStand.show_spisok()
    newIceCreamStand.proverka_flavor("Шоколадное")

    class IceCreamStick(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, hours):
            self.flavors = flavors
            self.location = location
            self.hours = hours

        def stick(self):
            print("Список мороженого на палочке:")
            for flavor in self.flavors:
                print(flavor, "мороженое на палочке")

    class IceCreamSoft(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, hours):
            self.flavors = flavors
            self.location = location
            self.hours = hours

        def soft(self):
            print("Список мягкого мороженого:")
            for flavor in self.flavors:
                print(flavor, "мягкое мороженое")



    newIceStick = IceCreamStick("Мороженое", "Кафе маороженое",["Фруктовое","Клубничное","Шоколадное"],"улица Пушкина 3","0:00-6:00")
    newIceSoft = IceCreamSoft("Мороженое", "Кафе маороженое",["Фруктовое","Клубничное","Шоколадное"],"улица Пушкина 3","0:00-6:00")
    IceCreamStick.stick(newIceSoft)
    IceCreamSoft.soft(newIceStick)

from tkinter import *
def z3():
    class IceCreamStand:
        def __init__(self, flavors):
            self.flavors = flavors

        def show_flavors(self):
            print("Cорта в наличии")
            for flavor in self.flavors:
                print(flavor)

    newIceCream = IceCreamStand(["Фруктовое", "Шоколадное", "Ванильное","Пломбир"])
    newIceCream.show_flavors()

    class IceCream:
        def __init__(self, flavors):
            self.ice_cream_stand = IceCreamStand(flavors)
            self.window = Tk()
            self.window.title("Мороженое")

            self.label = Label(self.window, text="Сорта в наличии:")
            self.label.pack()

            self.listbox = Listbox(self.window)
            for flavor in self.ice_cream_stand.flavors:
                self.listbox.insert(END, flavor)
            self.listbox.pack()

            mainloop()

    IceCream(["Фруктовое", "Шоколадное", "Ванильное","Пломбир"])

