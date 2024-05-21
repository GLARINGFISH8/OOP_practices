# №1

# class Patient:
#     def __init__(self, Full_name: str, age: int, disease: str,):
#
#         self.Full_name = Full_name
#         self.age = age
#         self.disease = disease
#
#     def record_reception(self, day, time):
#         print(f"вы записаны на {day} день, на {time} часов")
#
#
#     def status_patient(self):
#         print(f"ФИО - {self.Full_name}, возраст - {self.age}, болезнь - {self.disease}")



# №2

# class TouristSpot:
#     def __init__(self, place: str, country: str, type_Sigh: str, name_Sigh: str ):
#
#         self.place = place
#         self.country = country
#         self.type_Sigh = type_Sigh
#         self.name_Sigh = name_Sigh
#
#
#     def visit_place(self, name_tourist: str):
#         print(f"турист по имени {name_tourist}, посетил достопремечательность - {self.name_Sigh}")
#
#
#     def status_TouristSpot(self):
#         print(f"место - {self.place}, страна - {self.country},\n"
#               f"название достопримечательности - {self.name_Sigh},\n"
#               f"тип достопримечательности - {self.type_Sigh}")
#
#


# №3

# class ModelWindow:
#     def __init__(self, heading: str, coordin_left_upper_corner: list,
#                  size_vertical: int, size_horizont: int, color: str,
#                  status_visibility: bool, status_frame: bool):
#
#         self.heading = heading
#         self.coordin_left_corner = coordin_left_upper_corner
#         self.size_vetical = size_vertical
#         self.size_horizont = size_horizont
#         self.color = color
#         self.status_visibitity = status_visibility
#         self.status_frame = status_frame
#
#
# # функция изменения кординат окна по вертикали и горизонтали
#     def change_coordin_window(self, new_coordin):
#
#         if self.check_coordin_window(new_coordin) and self.check_admissions_size(new_coordin) == True:
#             self.coordin_left_corner = new_coordin
#
#
#
# # проверка переменной данных на тип list и на количество координат
#     def check_coordin_window(self, coordin):
#         if isinstance(coordin, list) and len(coordin) == 2:
#             return True
#
#         else:
#            print("error")
#
#            return False
#
#
#
# # проверка на область допустимых значений
#     def check_admissions_size(self, new_expansion):
#
#         if self.check_type(new_expansion, int) == True:
#             if new_expansion < 1960 and new_expansion < 1080:
#
#
#              return True
#
#
#
#
#             # если изменяем расположение окна, то идет проверка числа  на привышение допустимых значений
#         if  self.check_type(new_expansion, list) == True:
#
#             if (new_expansion[0] < 1960 and new_expansion[0] < 1080) and (
#                     new_expansion[1] < 1960 and new_expansion[1] < 1080):
#                 return True
#
#
#         # если тип не соответстувет ни одному из написаных выриантов
#         else:
#             return False
#
#
#
#
#
# # измененине расширение окна по горизонтали
#     def change_horizont(self, new_size: int):
#         if self.check_type(new_size, int) and self.check_admissions_size(new_size) == True:
#
#             self.size_horizont = new_size
#
#
# # изменение расширение окна по вертикали
#     def change_vertical(self, new_size: int):
#         if self.check_type(new_size, int) and self.check_admissions_size(new_size) == True:
#
#             self.size_vetical = new_size
#
#
#
#
# # проверка типа данных
#     def check_type(self, size, type):
#         if isinstance(size, type) == True :
#
#             return True
#
#         else:
#
#             return False
#
#
# # изменение цвета
#     def change_color(self, new_color: str):
#         if self.check_type(new_color, str) == True:
#
#             self.color = new_color
#
#
# # изменение состояния видимое/невидимое
#     def change_status_visibitity(self, other_status):
#         if self.check_type(other_status, bool):
#
#             self.status_visibitity = other_status
#
#
# # изменение состояния с рабкой/без рамки
#     def change_status_frame(self, other_status):
#         if self.check_type(other_status, bool) == True:
#
#             self.status_frame = other_status
#
#
# # выводит все поля класса
#     def status_ModelWindow(self):
#         print(f"заголовок окна - {self.heading}, координаты левого верхнего угла - {self.coordin_left_corner}\n"
#               f"размер по горизонтали - {self.size_horizont}, размер по вертикали - {self.size_vetical}\n"
#               f"цвет окна - {self.color}, состояние видимое/невидимое - {self.status_visibitity}\n"
#               f"состояние с рамкой/без рамки - {self.status_frame}")




# №4

#
# class ArrayUtils:
#     @staticmethod
# # ПРОВЕРКА
#
# # проверяет на тип list и проверака на тип данных элемента массива
#     def check_massiv(massiv: list):
#         if isinstance(massiv,  list):
#
#             for i in range(0, len(massiv), 1):
#
#                 if isinstance(massiv[i], int):
#                     return True
#
#             return False
#
#
#
#
# # БАЗОВЫЕ АЛГОРИТМЫ
#
# # нахождение суммы всех элементов массива
#     def sum_list(massiv: list):
#         if ArrayUtils.check_massiv(massiv) == True:
#
#                 sum_elem = 0
#
#                 for i in range(0, len(massiv), 1):
#                     sum_elem += massiv[i]
#
#                 return sum_elem
#
#
#
# # нахождение произведения всех элементов массива
#     def multi_list(massiv: list):
#         if ArrayUtils.check_massiv(massiv) == True:
#             multi_elem = 1
#
#             for i in range(0, len(massiv), 1):
#                 multi_elem *= massiv[i]
#
#             return multi_elem
#
#
# # инверсия массива
#     def inversion_list(massiv: list):
#         if ArrayUtils.check_massiv(massiv) == True:
#
#             new_list = []
#
#             for i in range(0, len(massiv), 1):
#                 item = massiv[-i - 1]
#                 new_list.append(item)
#
#             return new_list
#
#
# # нахождение максимального элемента массива
#
#     def finding_max(massiv: list):
#         if ArrayUtils.check_massiv(massiv) == True:
#
#             max_elem = massiv[0]
#
#             for i in range(0, len(massiv), 1):
#
#                 if max_elem < massiv[i]:
#                     max_elem = massiv[i]
#
#             return max_elem
#
#
# # нахождение минимального элемента массива
#
#     def finding_min(massiv: list):
#         if ArrayUtils.check_massiv(massiv) == True:
#
#             min_elem = massiv[0]
#
#             for i in range(0, len(massiv), 1):
#
#                 if min_elem > massiv[i]:
#                     massiv = massiv[i]
#
#             return min_elem


# №5

#
# class Vector:
#     def __init__(self, x: float, y: float, z: float):
#
#         self.x = x
#         self.y = y
#         self.z = z
#
# # сложение векторов
#     def __add__(self, other):
#
#         one_coordin = self.x + other.x
#         two_coordin = self.y + other.y
#         fri_coordin = self.z + other.z
#
#         new_vector = Vector(one_coordin, two_coordin, fri_coordin)
#
#         return new_vector
#
# # вычитание векторов
#     def __sub__(self, other):
#
#         one_coordin = self.x - other.x
#         two_coordin = self.y - other.y
#         fri_coordin = self.z - other.z
#
#         new_vector = Vector(one_coordin, two_coordin, fri_coordin)
#
#         return new_vector
#
# # скалярное произведение векторов
#     def __mul__(self, other):
#
#         one_coordin_mul = self.x * other.x
#         two_coordin_mul = self.y * other.y
#         fri_coordin_mul = self.z * other.z
#
#         rez_mul = one_coordin_mul + two_coordin_mul + fri_coordin_mul
#
#         return rez_mul
#
#
#
# # длинна вектора
#     def length_vector(self):
#
#         rez_legth = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 1/2
#
#         return rez_legth
#
#
# # вывод на экран
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"



# №6

#
# # ДАННЫЕ -> ПРОВЕРКА -> ПРИВЕДЕНИЕ К ОБЩЕМУ ЗНАМЕНАТЕЛЮ -> ПЕРЕДАЧА ДАННЫХ "ДЕЙСТВИЯ С ДРОБЯМИ"
#
# class Fraction:
#     def __init__(self, numerator: int, denominator: int):
#
#         self.numerator = numerator
#         self.denominator = denominator
#
#
#
# ### ДЕЙСТВИЯ С ДРОБЯМИ
#
#  # сложение дробей
#     def __add__(self, other):
#         fraction = self.convert_fraction(other)
#         if fraction != None:
#
#             rez_calculat = fraction[0].numerator + fraction[1].numerator
#
#             new_fract = Fraction(rez_calculat, fraction[0].denominator)
#
#             return new_fract
#
#         else:
#             print("ошибка")
#
#
#
# # вычитание дробей
#
#     def __sub__(self, other):
#         fraction = self.convert_fraction(other)
#         if fraction != None:
#             rez_calculat = fraction[0].numerator - fraction[1].numerator
#
#             new_fract = Fraction(rez_calculat, fraction[0].denominator)
#
#             return new_fract
#
#         else:
#             print("ошибка")
#
#
#
# # умножение дробей
#     def __mul__(self, other):
#         if self.check_denominator_NotZero(self.denominator) and self.check_denominator_NotZero(
#                 other.denominator) == True:
#
#             new_frac_mul = self.numerator * other.numerator
#             new_frac_den = self.denominator * other.denominator
#
#             new_fract = Fraction(new_frac_mul, new_frac_den)
#
#             return new_fract
#
#         else:
#             print("ошибка")
#
#
# # вывод дроби
#     def __str__(self):
#
#         if self.denominator == 1:
#
#             return f"{self.numerator}"
#
#         else:
#
#             return f"{self.numerator} {self.denominator} "
#
#
# ### ОСНОВНАЯ ЛОГИКА
#
#
# # приведение к общему знаменателю
#     def ghost_general_denominator(self, other):
#
#         fraction1_num = self.numerator * other.denominator
#         fraction1_denom = self.denominator * other.denominator
#
#         fraction2_num = other.numerator * self.denominator
#         fraction2_demom = other.denominator * self.denominator
#
#         identiс_fraction1 = Fraction(fraction1_num, fraction1_denom)
#         identic_fraction2 = Fraction(fraction2_num, fraction2_demom)
#
#         fraction_list =[identiс_fraction1,identic_fraction2]
#
#         return fraction_list
#
# # преобразование дроби, для дальнейших вычеслений
#     def convert_fraction(self, other):
#         if self.check_denominator_NotZero(self.denominator) and self.check_denominator_NotZero(other.denominator) == True:
#
#             if self.check_equality_denominator(self.denominator, other.denominator) == False:
#                 list_fraction = self.ghost_general_denominator(other)
#
#                 return list_fraction
#
#             else:
#
#                 temporary_fraction1 = Fraction(self.numerator, self.denominator)
#                 temporary_fraction2 = Fraction(other.numerator, other.denominator)
#
#                 ordinary_list_fraction = [temporary_fraction1, temporary_fraction2]
#
#                 return ordinary_list_fraction
#
#         else:
#
#             return None
#
#
# ### ПРОВЕРКА
#
# # проверка знаменателя на != 0
#     def check_denominator_NotZero(self, denominator):
#         if denominator != 0:
#
#             return True
#
#         else:
#
#             return False
#
#
# # проверка знаменателей на равенство
#     def check_equality_denominator(self, denominator1, denominator2):
#         if denominator1 == denominator2:
#
#             return True
#
#         else:
#             return False



# №7

#
# class GeometryUtils:
#     @staticmethod
#
#
#
# ## МЕТОДЫ ДЛЯ РАСЧЕТА ПЛОЩАДЕЙ
#
# # ПЛОЩАДЬ КРУГА
#
#     def square_circle(radius):
#
#         if GeometryUtils.check_type(radius, int) == True:
#             rezult = 3.14 * radius * 2
#
#             return rezult
#
#         else:
#
#             print("ошибка")
#
# # ПЕРИМЕТР КРУГА
#
#     def perimeter_circle(radius: int):
#
#         if GeometryUtils.check_type(radius, int) == True:
#             rezult = 2 * 3.14 * radius
#
#             return rezult
#
#         else:
#             print("ошибка")
#
#
# # ПЛОЩАДЬ ПРЯМОУГОЛЬНИКА
#
#     def sqiare_rectangle(long: int, width: int):
#         if GeometryUtils.check_type(long, int) and GeometryUtils.check_type(width, int) == True:
#             if GeometryUtils.check_negative(long) and GeometryUtils.check_negative(width) == True:
#
#                 rezult = long * width
#
#                 return rezult
#
#             else:
#                 print("ошибка")
#
#         else:
#             print("ошибка")
#
#
# # ПЕРИМЕТР ПРЯМОУГОЛЬНИКА
#
#     def  perimeter_ectangle(long: int, width: int):
#         if GeometryUtils.check_type(long, int) and GeometryUtils.check_type(width, int) == True:
#             if GeometryUtils.check_negative(long) and GeometryUtils.check_negative(width) == True:
#
#
#                 rezult = 2 * (long * width)
#
#                 return rezult
#
#             else:
#                 print("ошибка")
#
#         else:
#             print("ошибка")
#
# # ПЛОЩАДЬ ТРЕУГОЛЬНИКА ПО ФОРМУЛЕ ГЕРОНА
#
#     def sqiare_triangle(one_side: int, two_side: int, fri_side: int):
#         if GeometryUtils.check_type(one_side, int) and GeometryUtils.check_type(two_side, int) and GeometryUtils.check_type(fri_side, int) == True:
#
#
#             if GeometryUtils.check_negative(one_side) and GeometryUtils.check_negative(two_side) and GeometryUtils.check_negative(fri_side) == True:
#
#
#                 p =  (one_side + two_side + fri_side) / 2
#
#                 rezult = (p * (p - one_side) * (p - two_side) * (p - fri_side)) ** 1/2
#
#                 return  rezult
#
#             else:
#
#                 print("ошибка")
#
#         else:
#
#             print("ошибка")
#
#
#
#
#
# ## ПРОВЕРКА
#     def check_type(element, type):
#         if isinstance(element, type):
#
#             return True
#
#         else:
#
#             False
#
#
#     def check_negative(element):
#         if element > 0:
#
#             return True
#
#         else:
#
#             return False



# №8

# в будущем


#
# class Programm:
#     @staticmethod
#
#     def main():

# №1
#         patient1 = Patient("Васильев Висилий Васильевич", 40, "лень")
#
#         patient1.record_reception(6,17)
#
#         patient1.status_patient()


# №2
#         tourist1 = TouristSpot("храм", "Россия", "национальный", "буддийски храм")
#
#         tourist1.visit_place("Ivan")
#         tourist1.status_TouristSpot()



# №3
#         window = ModelWindow("Начало", [5,6], 1000, 1900,"желтый", True, True)
#
#         window.status_ModelWindow()
#
#         window.change_coordin_window([7,8])
#
#         window.change_horizont(65)
#
#         window.change_vertical(54)
#
#         window.change_color("Голубой")
#
#         window.change_status_visibitity(False)
#
#         window.change_status_frame(False)
#
#         window.status_ModelWindow()


# №4

        # massiv = [1,2,3,4]
        #
        # ArrayUtils.sum_list(massiv)
        #
        # ArrayUtils.multi_list(massiv)
        #
        # ArrayUtils.inversion_list(massiv)
        #
        # ArrayUtils.finding_max(massiv)
        #
        # ArrayUtils.finding_min(massiv)


# №5

        # vector1 = Vector(5,6,7)
        # vector2 = Vector(7,8,9)
        #
        # print(vector1 + vector2)
        # print(vector1 - vector2)
        # print(vector1 * vector2)
        #
        # print(Vector.length_vector(vector1))


# №6

        # fract1 = Fraction(1,2)
        # fract2 = Fraction(1,3)
        #
        # print(fract1 + fract2)
        # print(fract1 - fract2)
        # print(fract1 * fract2)


# №7

        # print(GeometryUtils.square_circle(45))
        # print(GeometryUtils.perimeter_circle(50))
        # print(GeometryUtils.sqiare_rectangle(60,30))
        # print(GeometryUtils.perimeter_ectangle(40,30))
        # print(GeometryUtils.sqiare_triangle(40,30,20))


# №8
# необычный код...