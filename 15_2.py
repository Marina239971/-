class Animal:

    name=''

    def Eat(self):
        print("Ням-ням");

    def setName(self,newName):
        self.name=newName

    def getName(self):
        return self.name

    def makeNoize(self):
        print(self.name+' говорит Гррр')
    def __init__(self,newName):
        self.name=newName
        print('Родилось животное ',self.name)

Tiger=Animal('Ричард')
print(Tiger.getName())

Tiger.setName('Рик')
print(Tiger.getName())

Tiger.Eat()
Tiger.makeNoize()
