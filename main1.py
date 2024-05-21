# №1
class Animal:
    def __init__(self, name: str, view: str, age: int, sound:str):
        self.name = name
        self.view = view
        self.age = age
        self.sound = sound

    def sound_publish(self):
        return  self.sound


    def conclusion_Characteristics(self):
        print(f"имя - {self.name}, вид - {self.view}, возраст - {self.age}, может сказать {self.sound}")






# №2

class Book:
    def __init__(self, name: str, Author: str, quantity_paged: int):
        self.name = name
        self.Author = Author
        self.quantity_paged = quantity_paged


    def open_paged(self, paged: int):
        paged = str(paged)
        if paged.isdigit() == True:
            paged = int(paged)

            if paged <= self.quantity_paged:
                print("страница успешно открыта")

            else:
                print("номер выходит за диапозон допустимых страниц")
        else:
            print("error")

    def status_book(self):
        print(f"название книги - {self.name}, Автор книги - {self.Author}, количество страниц - {self. quantity_paged} ")





# №3

class PassengerPlane:
    def __init__(self, manufacturer: str, model: str, сapacity: int,
quantity_passengers: int, height: int, speed: int):

        self.manufacturer = manufacturer
        self.model = model
        self.сapacity = сapacity
        self.quantity_passangers = quantity_passengers
        self.height = height
        self.speed = speed

    def Plane_takeoff(self):
        print("самолет взлетел")

    def Plane_landing(self):
        print("самолет совершил посадку")


    def Speed_change(self, new_speed:int):
        new_speed = str(new_speed)
        if new_speed.isdigit() == True:
            self.speed = new_speed

        else:
            print("error")


    def Height_change(self, new_hight: int):
        new_hight = str(new_hight)
        if new_hight.isdigit() == True:
            self.height = new_hight

        else:
            print("error")


    def Status_Plane(self):
        print(f"имя произовидетя - {self.manufacturer}, модель - {self.model}, вместительность - {self.сapacity},\n"
              f" количество пассажиров - {self.quantity_passangers},высота - {self.height}, скорость - {self.speed}")





# №4

class MusicAlbum:
    def __init__(self, executor: str, album: str, genre: str, list_track: list):
        self.executor = executor
        self.album = album
        self.genre = genre
        self.list_track = list_track


    def checking_track(self, track: str):
        track = str(track)

        if track.isdigit() == True:
            return False

        else:
            return True



    def Track_add(self, track: str):
        if self.checking_track(track) == True:
            self.list_track.append(track)

    def Track_delete(self, track: str):

        if self.checking_track(track) == True:
            new_list_track = []

            for i in range(0, len(self.list_track), 1):
                    if track != self.list_track[i]:
                        new_list_track.append(self.list_track[i])

        self.list_track = new_list_track


    def playback_track(self, track: str):
        if self.checking_track(track) == True:
            start = 0
            for i in self.list_track:
                if i == track:
                    start += 1
            if start == 1:
                print(f"трек под название {track}, воспроизводиться")

            else:
                print("error")


    def Statys_MisicAlbom(self):
        print(f"исполнитель - {self.executor}, название альбома - {self.album}\n"
              f", жанр - {self.genre}, список треков - {self.list_track}")













class Programm:
    @staticmethod
    def main():

# №1
        cat = Animal("Бакс", "Кот", 3, "мяу мяу")

        # вывод звука
        sound = cat.sound_publish()
        print(sound)

        # вывод характеристик
        status = cat.conclusion_Characteristics()



# №2
        book = Book("LIFE", "Kristofer", 100)

        # вызов метода по запросу страниц
        book.open_paged(100)

        # вызов метода статус книги
        book.status_book()




# №3
        plane = PassengerPlane("Sam", "65x", 100, 50, 45, 1000)

        # взлет самолета
        plane.Plane_takeoff()

        # посадка самолета
        plane.Plane_landing()

        # изменение высоты и скорости
        plane.Status_Plane()

        plane.Speed_change(500)

        plane.Height_change(100000)

        plane.Status_Plane()




# №4
        album = MusicAlbum("Джеймс Алан", "Through the Never", "Rok", ["Fuel", "one", "Cyanide"])

        # первоночальное состояние альбома
        album.Statys_MisicAlbom()

        # Добавляем в альбом трек
        album.Track_add("battery")
        album.Statys_MisicAlbom()

        # запускаем этот трек
        album.playback_track("battery")

        # удаляем трек
        album.Track_delete("battery")
        album.Statys_MisicAlbom()













