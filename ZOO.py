class Zoo():
    def __init__(self,name,hunger,boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        print('Появилась новая зверюшка - ',self.name)

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def talk(self):
        print('Привет! Меня зовут ', self.name, " . Сейчас я чувствую себя ", self.mood, "\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Thanks!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("OMG!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "норм"
        elif 10 < unhappiness <= 15:
            m = "пойдет"
        else:
            m = "ужасно"
        return m

def main():
    animal_name=input('Введите Имя (Если животных больше нет введите 0) ')
    while animal_name != '0':
        animal_hunger=input('Введите сытость зверя ')
        animal_boredom=input('Введитие уровень скуки ')
        animal=Zoo(animal_name,animal_hunger,animal_boredom)
        while k !='0':
            print \
                ("""
                    Моя зверюшка
                    0 - Ввести новое имя
                    1 - Узнать о самочувствиии зверюшки
                    2 - Покормить зверюшку
                    3 - Поиграть со зверюшкой
                    """)
            k=input()
            if k == "0":
                print("До свидания!")
            elif k == "1":
                animal.talk()
            elif k == "2":
                animal.eat()
            elif k == "3":
                animal.play()
            else:
                print("Извините, в меню игры нет такого пункта ", k)

        animal_name=input('Введите Имя (Если животных больше нет введите 0) ')
main()