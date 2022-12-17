class human():
    def __init__(self, name, age, momey):
        self.name = 'Oleg'
        self.age = '23'
        self.money = '150000$'
        self.job = 'Програміст'
        self.car = 'Mercedes'
    def age_of_human(self, year):
        self.age += year
    human.age_of_human(23)
    print(human.age)
    def money(self):
        self.money += 2000$
        human.money_of_human(150000$)
        print(human.money)


class House():
    def __init__(self, street, number):
        self.street = street
        self.number = number
        self.age = 0
    def build(self):
        print("Будинок на вулиці " + self.street + "під номером " + self.number + "побудований")
    def age_of_house(self, year):
        self.age += year



House1 = House("Carnaby Street", 11)
House2 = House("Carnaby street", 12)

House1.age_of_house(2)
print(House1.age)



