

class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def run(self):
        print("Run")

    def greet(self):
        print(f'Hello, {self.name}')

    def age(self):
        print(' {} is {} years old'.format(self.name,self.age))

player1 = PlayerCharacter("John", 30)

player1.run()
player1.greet()
player1.age()
