# №2
class Library:
    def __init__(self, Name: str, Address, List_book: list, List_employee: list):

        self.__Name = Name
        self.__Address = Address
        self.__List_book = List_book
        self.__List_employee = List_employee

# ГЕТТЕРЫ

    def get_name(self):
        return self.__Name

    def get_Address(self):
        return self.__Address

    def get_books(self):
        return self.__List_book

    def get_emploees(self):
        return self.__List_employee

# СЕТТЕРЫ

    def det_addreas(self, addreas: str):

        if isinstance(addreas, str):
            self.__Address = addreas

        else:
            print("error")

# ДРУГИЕ МЕТОДЫ

    def add_book(self, book: object):

        if isinstance(book, object) and self.__List_book.count(book) == 0:
            self.__List_book.append(book)

        else:
            return "error"

    def remove_book(self, book: object):

        if isinstance(book, object) and self.__List_book.count(book) == 1:

            new_list_book = []

            for i in self.__List_book:
                if i != book:
                    new_list_book.append(i)

            self.__List_book = new_list_book


        else:
            return "error"

    def add_employee(self, employee: object):

        if isinstance(employee, object) and self.__List_employee.count(employee) == 0:
            self.__List_employee.append(employee)

        else:
            return "error"


    def removee_employee(self, employee: object):

        if isinstance(employee, object) and self.__List_employee.count(employee) == 1:

            new_list_employee = []

            for i in self.__List_employee:
                if i != employee:
                    new_list_employee.append(i)

            self.__List_employee = new_list_employee


    def __str__(self):
        return (f"Имя - {self.__Name}\n"
                f"адрес - {self.__Address}\n"
                f"список книг - {self.__List_book}\n"
                f"список сотрудников - {self.__List_employee}")


class Book:

    def __init__(self, Name: str, Author: None or str, Year: int,  ID: int,
                 List_genre: list):

        self.__Name = Name
        self.__Author = Author
        self.__Year = Year
        self.__ID = ID
        self.__List_genre = List_genre


# ГЕТТЕРЫ

    def get_title(self):
        return self.__Name


    def get_author(self):
        return self.__Author

    def get_year(self):
        return self.__Year

    def get_id(self):
        return self.__ID

    def get_genres(self):
        return self.__List_genre


# СЕТТЕРЫ

    def set_year(self, year: int):

        if isinstance(year, int) and year > 0:

            self.__Year = year

        else:
            print("error")


# ДРУГИЕ МЕТОДЫ

    def add_genre(self, genre: object):

        if isinstance(genre, object) and self.__List_genre.count(genre) == 0:
            self.__List_genre.append(genre)

        else:
            return "error"


    def remove_genre(self, genre: object):

        if isinstance(genre, object) and self.__List_genre.count(genre) == 1:

            new_list_genre = []

            for i in self.__List_genre:

                if i != genre:
                    new_list_genre.append(i)

            self.__List_genre == new_list_genre

        else:
            return "error"


    def __str__(self):
        return (f"Имя - {self.__Name}\n"
                f"Автор - {self.__Author}\n"
                f"год - {self.__Year}\n"
                f"список жанров - {self.__List_genre}")

class Employee:

    def __init__(self, Name: str, Post: str, ID: int,
                 Contact_info: list):

        self.__Name = Name
        self.__Post = Post
        self.__ID = ID
        self.__Contact_info = Contact_info



# ГЕТТЕРЫ

    def get_name(self):
        return self.__Name

    def get_position(self):
        return self.__Post

    def get_id(self):
        return self.__ID

    def get_contact_info(self):
        return self.__Contact_info


# СЕТТЕРЫ

    def set_position(self, position: str):

        if isinstance(position, str):
            self.__Post == position

        else:
            print("error")

# ДРУГИЕ МЕТОДЫ

    def add_contact_info(self, contact_info: object):

        if isinstance(contact_info, object) and self.__Contact_info.count(contact_info) == 0:

            self.__Contact_info.append(contact_info)

        else:
            return "error"


    def remove_contact_info(self, contact_info: object):

        if isinstance(contact_info, object) and self.__Contact_info.count(contact_info) == 1:

            new_list_contact_info = []

            for i in self.__Contact_info:
                if i != contact_info:
                    new_list_contact_info.append(i)

            self.__Contact_info = new_list_contact_info

        else:
            return "error"


    def __str__(self):
        return (f"Имя - {self.__Name}\n"
                f"Должность - {self.__Post}\n"
                f"ID - {self.__ID}\n"
                f"контактная информация - {self.__Contact_info}")




class ContactInfo:

    def __init__(self, type_contact: str, value: str):

        self.__type_contact = type_contact
        self.__value = value


# ГЕТТЕРЫ

    def get_type(self):
        return self.__type_contact

    def get_value(self):
        return self.__value

# СЕТТЕРЫ

    def set_type_contact(self, type_contact: str):

        if isinstance(type_contact, str):
            self.__type_contact = type_contact

        else:
            print("error")


    def set_value(self, value: str):

        if isinstance(value, str):
            self.__value = value

        else:
            print("ошибка")

# ДРУГИЕ МЕТОДЫ

    def __str__(self):
        return (f"тип - {self.__type_contact}\n"
                f"значение - {self.__value}")



class Genre:

    def __init__(self, Name: str, Description: str):

        self.__Name = Name
        self.__Description = Description



# ГЕТТЕРЫ

    def get_name(self):
        return self.__Name

    def get_description(self):
        return self.__Description

# СЕТТЕРЫ

    def set_name(self, name: str):

        if isinstance(name, str):
            self.__Name = name

        else:
            print("error")

    def set_description(self, description: str):

        if isinstance(description, str):
            self.__Description = description

        else:
            print("error")

# ДРУГИЕ МЕТОДЫ

    def __str__(self):
        return (f"Имя - {self.__Name}\n"
                f"Описание - {self.__Description}")





class Programm:
    @staticmethod

    def main(self):

# СОЗДАНИЕ ОБЪЕКТА
        genre = Genre("Fantastic", "ochen zanimatelno")
        contact = ContactInfo("mail", " highest meaning")


        book = Book("Kara", "D.V.Rak",
                    2015, 99999, [])

        employee = Employee("Pasha", "vahter",
                            11111, [])

        lib = Library("Simply", "Simple",
                      [], [])

# МАНИПУЛЯЦИИ НАД ОБЪЕКТАМИ

        book.add_genre(genre)
        employee.add_contact_info(contact)


        lib.add_book(book)
        lib.add_employee(employee)

        print(lib)





# №3
class Car:

    def __init__(self, brand: str, model: str,
                 year_release: int, price: int,
                 status: str):

        self.__brand = brand
        self.__model = model
        self.__year_release = year_release
        self.__price = price
        self.__status = status



# ГЕТТЕРЫ

    def get_brand(self):
        return self.__brand


    def get_model(self):
        return self.__model


    def get_year_release(self):
        return self.__year_release


    def get_price(self):
        return self.__price


    def get_status(self):
        return self.__status



# СЕТТЕРЫ

    def set_price(self, price: int):

        if isinstance(price, int):
            self.__price = price

        else:
            print("error")


    def _set_status(self, status: str):

        if isinstance(status, str):
            self.__status = status

        else:
            print("error")




# ДРУГИЕ МЕТОДЫ

    def __str__(self):

        return (f"бренд - {self.__brand}\n"
                f"модель - {self.__model}\n"
                f"год выхода - {self.__year_release}\n"
                f"цена - {self.__price}\n"
                f"состояние - {self.__status}")


class Salesperson:

    def __init__(self, name: str, experience: int,
                 list_car_sold: list):

        self.__name = name
        self.__experience = experience
        self.__list_car_sold = list_car_sold


# ГЕТТЕРЫ

    def get_name(self):
        return self.__name


    def get_experience(self):
        return self.__experience


    def get_list_car_sold(self):
        return self.__list_car_sold


#  СЕТТЕРЫ

    def _set_list_car_sold(self, list_car_sold: list):

        if isinstance(list_car_sold, list):
            self.__list_car_sold = list_car_sold

        else:
            print("error")

#  ДРУГИЕ МЕТОДЫ

    def add_list_car_sold(self, car: object):

        if isinstance(car, object) and self.__list_car_sold.count(car) == 0:
            self.__list_car_sold.append(car)

        else:
            return "error"


    def remove_list_car_sold(self, car: object):

        if isinstance(car, object) and self.__list_car_sold.count(car) == 1:

            new_list_car_sold = []

            for i in self.__list_car_sold:

                if i != car:
                    new_list_car_sold.append(i)

            Salesperson._set_list_car_sold(self, new_list_car_sold)

        else:
            return "error"



    def __str__(self):

        return (f"имя - {self.__name}\n"
                f"стаж - {self.__experience}\n"
                f"проданные автомобили - {self.__list_car_sold}")




class Customer:

    def __init__(self, name: str, phone: str,
                 mail: str, list_car_order: list):


        self.__name = name
        self.__phone = phone
        self.__mail = mail
        self.__list_car_order = list_car_order


# ГЕТТЕРЫ

    def get_name(self):
        return self.__name


    def get_phone(self):
        return self.__phone


    def get_mail(self):
        return self.__mail


    def get_list_car_order(self):
        return self.__list_car_order


# СЕТТЕРЫ

    def _set_list_car_order(self, list_car_order: list):

        if isinstance(list_car_order, list):
            self.__list_car_order = list_car_order

        else:
            print("error")


# ДРУГИЕ МЕТОДЫ

    def add_list_car_order(self, car: object):

        if isinstance(car, object) and self.__list_car_order.count(car) == 0:
            self.__list_car_order.append(car)

        else:
            return "error"


    def remove_list_car_order(self, car: object):

        if isinstance(car, object) and self.__list_car_order.count(car) == 0:

            new_list_car_order = []

            for i in self.__list_car_order:

                if i != car:
                    new_list_car_order.append(i)

            Customer._set_list_car_order(self, new_list_car_order)

        else:
            return "error"


    def __str__(self):

        return (f"имя - {self.__name}\n"
                f"телефон - {self.__phone}\n"
                f"почта - {self.__mail}\n"
                f"список купленных машин - {self.__list_car_order}")



class Dealership:

    def __init__(self, list_car_availability: list,
                 list_salesperson: list,
                 list_customer: list):

        self.__list_car_availability = list_car_availability
        self.__list_salesperson = list_salesperson
        self.__list_customer = list_customer



# ГЕТТЕРЫ

    def get_list_cat_availability(self):
        return self.__list_car_availability


    def get_list_saleperson(self):
        return self.__list_salesperson


    def get_list_customer(self):
        return self.__list_customer


# СЕТТЕРЫ

    def _set_list_car_availability(self, list_car_availability: list):

        if isinstance(list_car_availability, list):
            self.__list_car_availability = list_car_availability

        else:
            print("error")


    def _set_list_salesperson(self, list_salesperson: list):

        if isinstance(list_salesperson, list):
            self.__list_salesperson = list_salesperson

        else:
            print("error")




    def _set_list_customer(self, list_customer: list):

        if isinstance(list_customer, list):
            self.__list_customer = list_customer

        else:
            print("error")



    def add_list_car_availability(self, car: object):

        if isinstance(car, object) and self.__list_car_availability.count(car) == 0:
            self.__list_car_availability.append(car)

        else:
            return "error"



    def remove_list_car_availability(self, car: object):

        if isinstance(car, object) and self.__list_car_availability.count(car) == 1:

            new_list_car_availability = []

            for i in self.__list_car_availability:

                if i != car:
                    new_list_car_availability.append(i)


            Dealership._set_list_car_availability(self, new_list_car_availability)


        else:
            return "error"



    def add_list_salesperson(self, salesperson: object):

        if isinstance(salesperson, object) and self.__list_salesperson.count(salesperson) == 0:
            self.__list_salesperson.append(salesperson)

        else:
            return "error"


    def remove_list_salesperson(self, salesperson: object):

        if isinstance(salesperson, object) and self.__list_salesperson.count(salesperson) == 1:

            new_list_salesperson = []

            for i in self.__list_salesperson:

                if i != salesperson:
                    new_list_salesperson.append(i)


            Dealership._set_list_salesperson(self, new_list_salesperson)


        else:
            print("error")




    def add_list_customer(self, customer: object):

        if isinstance(customer, object) and self.__list_customer.count(customer) == 0:
            self.__list_customer.append(customer)

        else:
            return "error"


    def remove_list_customer(self, customer: object):

        if isinstance(customer, object) and self.__list_customer.count(customer) == 1:

            new_list_customer = []

            for i in self.__list_customer:

                if i != customer:
                    new_list_customer.append(i)


            Dealership._set_list_customer(new_list_customer)

        else:
            return "error"



    def __str__(self):

        return (f"список машин в наличии - {self.__list_car_availability}\n"
                f"список продавцов - {self.__list_salesperson}\n"
                f"список покупателей - {self.__list_customer}")





class History:

    @staticmethod

    def main():

        print("ЭПИЛОГ\n")

        input("\nНажмите Enter, чтобы продолжить:\n")


        car1 = Car("Kara", "o123j", 2000, 100000, "в наличии")
        car2 = Car("Kara", "ax34", 2000, 200000, "в наличии")
        car3 = Car("Kara", "yto98", 2000, 300000, "в наличии")

        print(f"На заводе КАРА было создано три новых модели автомобилей\n")

        print(f"Первый автомобиль - {car1}\n")
        print(f"Второй автомобиль - {car2}\n")
        print(f"Третий автомобиль - {car3}")

        input("\nНажмите Enter, чтобы продолжить:\n")




        print("После производства их отправили в автосервис КАРАЛУЧШАЯ где они успешно были зарегестрированны")

        dealeship = Dealership([], [], [])

        dealeship.add_list_car_availability(car1)
        dealeship.add_list_car_availability(car2)
        dealeship.add_list_car_availability(car3)

        input("\nНажмите Enter, чтобы продолжить:\n")



        salespers1 = Salesperson("Oleg", 0, [])
        salespers2 = Salesperson("Bogdan", 0, [])
        salespers3 = Salesperson("Valentin", 0, [])

        print("Тем временем в автосервис 'КАРАЛУЧШАЯ' поступило три новых продавца\n")

        print(f"Первый сотрудник - {salespers1}\n")
        print(f"Второй сотрудник - {salespers2}\n")
        print(f"Третий сотрудник - {salespers3}\n")


        input("\nНажмите Enter, чтобы продолжить:\n")

        print("все три сотрудника были успешно добавлены в базу данных")
        dealeship.add_list_salesperson(salespers1)
        dealeship.add_list_salesperson(salespers2)
        dealeship.add_list_salesperson(salespers2)



        input("\nНажмите Enter, чтобы продолжить:\n")

        custom1 = Customer("Padsha", "+77495643209", "@kara", [])
        custom2 = Customer("Ravet", "+789065871984", "@kara", [])
        custom3 = Customer("Igor", "+712593959091", "@kara", [])

        print("Также в сервис пришли три новых покупателя\n")

        print(f"Первый покупатель - {custom1}\n")
        print(f"Второй покупатель - {custom2}\n")
        print(f"Третий покупатель - {custom3}\n")


        input("\nНажмите Enter, чтобы продолжить:\n")


        print("все три покупателя были успешно зарегестрированы\n")
        dealeship.add_list_customer(custom1)
        dealeship.add_list_customer(custom2)
        dealeship.add_list_customer(custom3)

        print("\nКОНЕЦ ЭПИЛОГА\n")

        input("\nНажмите Enter, чтобы продолжить:\n")



        print("ЭПИЗОД ПЕРВЫЙ")

        input("\nНажмите Enter, чтобы продолжить:\n")



        print(f"между покупателем {custom1.get_name()}  и продавцом {salespers1.get_name()} завязался разговор.\n"
              f"В ходе которого покупатель {custom1.get_name()} решил купить автомобиль бренда {car1.get_brand()}\n"
              f"и модели {car1.get_model()} по цене в {car1.get_price()}.\n"
              f"CДЕЛАКА БЫЛА ЗАКЛЮЧЕНА!!!!")



        dealeship.remove_list_car_availability(car1) # удаляем из списка "машин в наличии" купленную машину
        salespers1.add_list_car_sold(car1) # Можем поздравить salespers1!!! Он продал свою первую машину !!!
        custom1.add_list_car_order(car1) # Также можем поздравить и custom1 с приобретенным автомобилем !!!

        input("\nНажмите Enter, чтобы продолжить:\n")

        print("КОНЕЦ ПЕРВОГО ЭПИЗОДА")


        input("\nНажмите Enter, чтобы продолжить:\n")

        print("ВТОРОЙ ЭПИЗОД")

        nput("\nНажмите Enter, чтобы продолжить:\n")

        print("автосервив КАРАЛУЧШАЯ случайно сгорел. На это наша история подходит к концу.")





History.main()


# №4

class HogwartsStudent:

    def __init__(self, name: str, house: str,
                 mana: int, list_study_spell: list):

        self.__name = name
        self.__house = house
        self.__mana = mana
        self.__list_study_spell = list_study_spell



# ГЕТТЕРЫ

    def get_name(self):
        return self.__name


    def get_house(self):
        return self.__house


    def get_mana(self):
        return self.__mana


    def get_study_spell(self):
        return self.__list_study_spell


# СЕТТЕРЫ

    def set_name(self, name: str):

        if isinstance(name, str):
            return self.__name

        else:
            print("error")


    def set_house(self, house: str):

        if isinstance(house, str):
            self.__house = house

        else:
            print("error")


    def set_mana(self, mana: int):

        if isinstance(mana, int):
            self.__mana = mana


        else:
            print("error")


    def __set_list_study_spell(self, list_study_spell: list):

        if isinstance(list_study_spell, list):
            self.__list_study_spell = list_study_spell

        else:
            print("error")




# ДРУГИЕ МЕТОДЫ


    def learn_spell(self, spell: Spell):

        if isinstance(spell, object) and self.__list_study_spell.count(spell) == 0:
            self.__list_study_spell.append(spell)

        else:
            return "error"


 # НАПИСАТЬ ЕЩЕ ОДИН МЕТОДЫ



class Spell:



    def __init__(self, name: str, descrip_effect: str, mana_cost: int):

         self.__name = name
         self.__descrip_effect = descrip_effect
         self.__mana_cost = mana_cost



# ГЕТТЕРЫ

    def get_name(self):
        return self.__name


    def get_descrip_effect(self):
        return self.__descrip_effect


    def get_mana_cost(self):
        return self.__mana_cost


# СЕТТЕРЫ

    def set_name(self, name: str):

        if isinstance(name, str):
            self.__name = name

        else:
            print("error")


    def set_descrip_effect(self, descrip_effect: str):

        if isinstance(descrip_effect, str):
            self.__descrip_effect = descrip_effect

        else:
            print("error")


    def set_mana_cost(self, mana_cost: int):

        if isinstance(mana_cost, int):
            self.__mana_cost = mana_cost

        else:
            print("error")

    def cast(self, target: HogwartsStudent):

      pass


