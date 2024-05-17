# №1

struct Animal:
    name: str
    Viev: str
    age: int
    weight: float
    vaccine: bool

dog1 = Animal("Sharik", "Dog", 20,  100.1, True)
cat1 = Animal("Merzik", "Cat", 30, 10.1, False)
hamster999 = Animal("Lord", "Hamster", 0, 1, True)




# №2

struct Artifact:
    material: str
    history_meaning: int
    streng: int


struct Date:
    Day: int
    Month: str
    year: int


struct Participants_society:
    name:str
    role: str
    clothes: str
    experience: int


Artifact1 = Artifact("rhodium", 100000, 100)
Artifact2 = ("iron" , 100 , 10)
Date1 = (10, "December", 1924 )
Participants_society1 = Participants_society("Horm", "Chairman", "Blak raincoat", 50 )
Participants_society2 = Participants_society("Kurt", " ordinary participant", "An old suit", 20)

history = (f"{Participants_society1} и {Participants_society2}, должны встретиться на собрании магов в {Date1} , и каждый из приглашенных должен взять свой артефакт,"
           f"у {Participants_society2} {Artifact2}, а у {Participants_society1} {Artifact1}."
           f"так как у {Participants_society2}, все хуже, чем у {Participants_society1} , {Participants_society2} из зависти, планирует убить своего старшего коллегу."
           f"И вот на собрании {Participants_society2} вонзает нож в спину {Participants_society1} и забирает у него {Artifact1}. на этом история окончена.")



# №3

struct Market:
    list_product: list


struct Fermer:
    name: str
    age: str



struct Product:
    name: str
    quantity: int
    price: int



struct Date:
    Day: int
    Month: str
    year: int


struct Client:
    name: str
    age: int
    specifications_demograph: str
    preferences: list
    col_money: int

otvet1 = ("допустип выбор в стуктуре Client в поле preferences, будет влиять на структуру Market. Фермеры будут продавать то ,что "
         "предпочитают покупатели, они не будут продавать товар, который не валидный. Также в этом выборе идет непосредственное"
         "влияние на рынок, в зависимости от предпочтений клиентов, рынок будет изобиливать теми или иными товарами!!!")


otvet2 = ("Еще один пример: если в структуре Client в поле col_money, данный атрибут будет оцениваться как <<мало денег>>, также допустим возможность"
          "что эта характеристика отражает финансовое положение всего общество, то влияние будет оказываться на структуру Produсt в поле price, то есть результат"
          "этого влияния будет пониженые цены на товары(клиентам просто не хватит денег, чтобы купить товар или товары будут продаваться не эффективно. "
          "верно и обратное, если у клиентов будет много денег, то цены на товары будут повыше!!!")

































