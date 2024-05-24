# №1
# #
# class Wizard:
#
#     def __init__(self, name_wizard: str, faculty: str, level_magic: int,
#                  lits_spell: list, status: str):
#
#         self.__name_wizard = name_wizard
#         self.__faculty = faculty
#         self.__level_magic = level_magic
#         self.__list_spell = lits_spell
#         self.__status = status
#
# # ГЕТТЕРЫ
#     def get_name(self):
#
#         return self.__name_wizard
#
#     def get_house(self):
#
#         return self.__faculty
#
#     def get_magic_level(self):
#
#         return self.__level_magic
#
#     def get_list_spells(self):
#
#         return self.__list_spell
#
#     def get_status(self):
#
#         return self.__status
#
#
# # СЕТТЕРЫ
#
#     def set_house(self, house: str):
#
#         if isinstance(house, str) == True:
#             self.__faculty = house
#
#         else:
#
#             print("error")
#
#
#     def set_magic_level(self, magic_level: int):
#
#         if isinstance(magic_level, int) and (magic_level >= 0):
#             self.__level_magic = magic_level
#
#         else:
#
#             print("error")
#
#
#     def set_status(self):
#
#             if self.__status == "в Хогвартсе":
#                 self.__status = "за пределами"
#
#             else:
#
#                 self.__status = "в Хогвартсе"
#
#
#
#
#
#
# # ДРУГИЕ МЕТОДЫ
#
#     def add_spell(self, spell):
#
#         if (isinstance(spell, object)) and (self.__list_spell.count(spell) == 0) == True: # ???????
#             self.__list_spell.append(spell)
#
#         else:
#
#             print("error")
#
#     def remove_spell(self, spell):
#         if self.__list_spell.count(spell) == 1:
#
#             new_list = []
#
#             for i in self.__list_spell:
#
#                 if i != spell:
#                     new_list.append(i)
#
#             self.__list_spell = new_list
#
#         else:
#
#             print("error")
#
#
#
#     def increase_macig_level(self, amount):
#         self.set_magic_level(amount)
#
#
#     def __str__(self):
#         return (f"имя волшебника - {self.__name_wizard}\n"
#               f"факультет - {self.__faculty}\n"
#               f"уровень магической силы - {self.__level_magic}\n"
#               f"список известных заклинаний - {self.__list_spell}\n"
#               f" статус - {self.__status}")
#
#
#
# # №1.2
#
# class Spell:
#
#     def __init__(self, name_spell: str, level_complexity: int,
#                  type_spell: str,):
#
#         self.__name_spell = name_spell
#         self.__level_complexity = level_complexity
#         self.__type_spell = type_spell
#
#
#
# # ГЕТТЕРЫ
#
#     def get_name_spell(self):
#
#         return self.__name_spell
#
#     def get_level_complexity(self):
#
#         return self.__level_complexity
#
#     def get_type_spell(self):
#
#         return self.__type_spell
#
#
# # СЕТТЕРЫ
#
#     def set_name_spell(self, new_name_spell):
#
#         if isinstance(new_name_spell, str):
#
#             self.__name_spell = new_name_spell
#
#     def set_level_complexity(self, new_level_complexity):
#
#         if isinstance(new_level_complexity, int):
#
#             self.__level_complexity = new_level_complexity
#
#
#     def set_type_spell(self, new_type_spell):
#
#         if isinstance(new_type_spell, str):
#
#             self.__type_spell = new_type_spell
#
#
#     def __str__(self):
#
#         return (f"название заклинания - {self.__name_spell}\n"
#               f"уровень заклинания - {self.__level_complexity}\n"
#               f"тип заклинания - {self.__type_spell}")
#



# №2

# class Employee:
#
#     def __init__(self, name_employee: str, post_employee: str,
#                  department: str, salary: int, experience: int,
#                  list_done_work: list):
#
#         self.__name_employee = name_employee
#         self.__post_employee = post_employee
#         self.__department = department
#         self.__salary = salary
#         self.__experience = experience
#         self.__list_done_work = list_done_work
#
#
# # ГЕТТЕРЫ
#
#     def get_name_employee(self):
#
#         return self.__name_employee
#
#     def get_post_employee(self):
#
#         return self.__post_employee
#
#     def get_depatment(self):
#
#         return self.__department
#
#     def get_salary(self):
#
#         return self.__salary
#
#     def get_experience(self):
#
#         return self.__list_done_work
#
#
# # СЕТТЕРЫ
#
#     def set_name_employee(self, new_name: str):
#
#         if isinstance(new_name, str) == True:
#
#             self.__name_employee = new_name
#
#         else:
#
#             print("error")
#
#     def set_post_employee(self, new_post):
#
#         if isinstance(new_post, str) == True:
#
#             self.__post_employee = new_post
#
#         else:
#
#             print("error")
#
#     def set_department(self, new_depart):
#
#         if isinstance(new_depart, str):
#
#             self.__department = new_depart
#
#         else:
#
#             print("error")
#
#     def set_salary(self, new_salary):
#
#         if isinstance(new_salary, int) == True:
#
#             self.__salary = new_salary
#     def set_experience(self, new_experience):
#
#         if isinstance(new_experience, int) and new_experience > 0:
#
#             self.__experience = new_experience
#
#         else:
#
#             print("error")
#
# # ДРУГИЕ МЕТОДЫ
#
#     def add_list_done_work(self, project):
#
#         if isinstance(project, object)  and self.__list_done_work.count(project) == 0:
#
#             self.__list_done_work.append(project)
#
#     def del_list_done_work(self, project):
#
#         if isinstance(project, object)  and self.__list_done_work.count(project) == 1:
#
#             new_list = []
#
#             for i in self.__list_done_work:
#
#                 if i != project:
#                     new_list.append(i)
#
#             self.__list_done_work = new_list
#
#         else:
#
#             print("error")
#
#
#
#     def add_salary(self, new_salary):
#
#         if new_salary > self.__salary:
#
#             self.set_salary(new_salary)
#
#         else:
#
#             print("error")
#
#     def __str__(self):
#         return (f"имя сотрудника - {self.__name_employee}\n"
#                 f"должность - {self.__post_employee}\n"
#                 f"отдел - {self.__department}\n"
#                 f"зарплата - {self.__salary}\n"
#                 f"стаж работы - {self.__experience}\n"
#                 f"список выполненых проектов - {self.__list_done_work}")
#
#
#
#
# class Project:
#
#     def __init__(self, name_projct: str, complexity: int, type: str):
#
#         self.__name_project = name_projct
#         self.__complexity = complexity
#         self.__type = type
#
# # ГЕТТЕРЫ
#     def get_name_project(self):
#
#         return self.__name_project
#
#     def get_complexity(self):
#
#         return self.__complexity
#
#     def get_type(self):
#
#         return self.__type
#
#
# # СЕТТЕРЫ
#
#     def set_name_project(self, new_name):
#
#         if isinstance(new_name, str) == True:
#
#             self.__name_project = new_name
#
#         else:
#
#             print("error")
#
#     def set_complexity(self, new_complexity):
#
#         if isinstance(new_complexity, int) == True:
#
#             self.__complexity = new_complexity
#
#         else:
#
#             print("error")
#
#     def set_type(self, new_type):
#
#         if isinstance(new_type, str):
#
#             self.__type = new_type
#
#         else:
#
#             print("error")
#
# # ДРУГИ МЕТОДЫ
#
#     def __str__(self):
#         return (f"название проекта - {self.__name_project}\n"
#                 f"сложность проекта - {self.__complexity}\n"
#                 f"тип проекта - {self.__type}")
#
#
#
# pr1 = Project("слежка", 10, "тяжелый")
# pr2 = Project("уборка", 5, "лекгий")
# pr3 = Project("конфронтация", 100, "мега hard")
#
# emp = Employee("Сергей", "вахтер",
#                "вахтерский", 200000,
#                15,[pr1, pr2])
#
#
# emp.set_name_employee("Алексей")
# emp.set_post_employee("Клинер")
# emp.set_department("Клинерский")
# emp.set_salary(500000)
# emp.set_experience(40)
#
# print(emp)
#
# emp.add_salary(5999999)
# emp.add_list_done_work(pr3)
# emp.del_list_done_work(pr1)
#
# print(emp)




# №3
#
# class Robot:
#
#     def __init__(self, serial_num: int, model: str, current_task: str,
#                  level_charge: int, status: bool):
#
#
#         self.__serial_num = serial_num
#         self.__model = model
#         self.__current_task = current_task
#         self.__level_charge = level_charge
#         self.__status = status
#
#
#
# # ГЕТТЕРЫ
#
#     def get_serial_num(self):
#
#         return self.__serial_num
#
#     def get_model(self):
#
#         return self.__model
#
#     def _get_current_task(self):
#
#         return self.__current_task
#
#     def get_level_charge(self):
#
#         return self.__level_charge
#
#     def get_status(self):
#
#         return self.__status
#
# # СЕТТЕРЫ
#
#     def set_serial_num(self, new_serial_num):
#
#         if isinstance(new_serial_num, int) and new_serial_num >= 0:
#
#             self.__serial_num = new_serial_num
#
#         else:
#
#             print("error")
#
#     def set_model(self, new_model):
#
#         if isinstance(new_model, str) == True:
#
#             self.__model = new_model
#
#         else:
#
#             print("error")
#
#     def set_current_task(self, new_current_task):
#
#         if isinstance(new_current_task, str) == True:
#
#             self.__current_task = new_current_task
#
#         else:
#
#             print("error")
#
#     def set_level_charge(self, new_level_charge):
#
#         if isinstance(new_level_charge, int) and new_level_charge > 0:
#             self.__level_charge = new_level_charge
#
#     def set_status(self):
#         if self.__status == True:
#
#             self.__status = False
#
#         else:
#
#             self.__status = True
#
# # ДРУГИЕ МЕТОДЫ
#
#     def __str__(self):
#         return (f"серийный номер - {self.__serial_num}\n"
#                 f"модель - {self.__model}\n"
#                 f"текущая задача - {self.__current_task}\n"
#                 f"уроверь заряда батареи - {self.__level_charge}\n"
#                 f"статус - {self.__status}")
#


# №4

# class Athlete:
#
#     def __init__(self, name_athlete: str, age: int, type_sport: str,
#                  list_achievement: list):
#
#         self.__name_athlete = name_athlete
#         self.__age = age
#         self.__type_sport = type_sport
#         self.__list_achievement = list_achievement
#
#
#
#
# # ГЕТТЕРЫ
#
#     def get_name_athlete(self):
#
#         return self.__name_athlete
#
#     def get_age(self):
#
#         return self.__age
#
#     def get_type_sport(self):
#
#         return self.__type_sport
#
#     def get_list_anchievement(self):
#
#         return self.__list_achievement
#
#
#
#
#
# # СЕТТЕРЫ
#     def set_name_athlete(self, new_name):
#
#         if isinstance(new_name, str) == True:
#
#             self.__name_athlete = new_name
#
#         else:
#
#             print("error")
#
#     def set_age(self, new_age):
#
#         if isinstance(new_age, int) and (new_age >= self.__age):
#
#             self.__age = new_age
#
#         else:
#
#             print("error")
#
#     def set_type_sport(self, new_type_sport):
#
#         if isinstance(new_type_sport, str) == True:
#
#             self.__type_sport = new_type_sport
#
#
#         else:
#
#             print("error")
#
# # ДРУГИЕ МЕТОДЫ
#
#     def add_achievement(self, achievement):
#
#         if isinstance(achievement, str) and self.__list_achievement.count(achievement) == 0:
#
#             self.__list_achievement.append(achievement)
#
#         else:
#
#             print("error")
#
#
#     def del_achievement(self, achievement):
#
#         if isinstance(achievement, str) and self.__list_achievement.count(achievement) == 1:
#
#             new_list = []
#
#             for i in self.__list_achievement:
#
#                 if i != achievement:
#                     new_list.append(i)
#
#             self.__list_achievement = new_list
#
#         else:
#
#             print("error")
#
#
#
#
#     def __str__(self):
#
#         return (f"имя атлета - {self.__name_athlete}\n"
#                 f"возраст - {self.__age}\n"
#                 f"вид спорта - {self.__type_sport}\n"
#                 f"достижения - {self.__list_achievement}")
#
#



class Programm:
    @staticmethod

    def main():



# №1
        spell1 = Spell("«Акцио", 2, "всопомогательный")
        spell2 = Spell("адское пламя", 7, "атакующая")
        spell3 = Spell("Вулнера санентур", 5, "лечебное")

        wiz = Wizard("Tach", "dragons",
                     10, [spell1, spell2],
                     "в Хогвартсе")

        print(wiz)

        wiz.set_house("hawks")
        wiz.set_magic_level(2)
        wiz.set_status()

        wiz.add_spell(spell3)
        wiz.remove_spell(spell2)

        print(wiz)


# № 1.2

        spell4 = Spell("Вулнера санентур", 5, "лечебное")

        spell4.set_name_spell("Аберто")
        spell4.set_level_complexity(1)
        spell4.set_type_spell("поддержка")

        print(spell4)
# № 2
        pr1 = Project("слежка", 10, "тяжелый")
        pr2 = Project("уборка", 5, "лекгий")
        pr3 = Project("конфронтация", 100, "мега hard")

        emp = Employee("Сергей", "вахтер",
                       "вахтерский", 200000,
                       15,[pr1, pr2])


        emp.set_name_employee("Алексей")
        emp.set_post_employee("Клинер")
        emp.set_department("Клинерский")
        emp.set_salary(500000)
        emp.set_experience(40)

        print(emp)

        emp.add_salary(5999999)
        emp.add_list_done_work(pr3)
        emp.del_list_done_work(pr1)

        print(emp)

# №3


        rob1 = Robot(1234, "45b5", "готовить",
                     50, True)

        rob1.set_serial_num(43211)
        rob1.set_model("54jk54")
        rob1.set_current_task("убирать")
        rob1.set_level_charge(30)
        rob1.set_status()
        print(rob1)


# №4

        ath = Athlete("Боб", 50, "бег",
                      ["первое место по бегу", "второе место по плаванию"])

        ath.set_name_athlete("Бобик")
        ath.set_age(60)
        ath.set_type_sport("плавание")

        ath.add_achievement("самый лучший плавец")
        ath.del_achievement("первое место по бегу")

        print(ath)





























