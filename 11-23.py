class Person:
    def __init__(self):
        self.name = 'Lebron'
        self.age = '39'
        self.position = 'SG'
        self.salary = '$99,023,288'
        self.team = 'Lakers'
        self.attack1 = 'dunk'
        self.attack2 = '3 points'
        self.enemy = 5


    def talk(self):
        print('I am {} , {} years old , play on {}'.format(self.name , self.age , self.position))

    def attack(self):  
        if self.enemy == 0 :
            print(self.attack1)
        if self.enemy > 2:
            print(self.attack2)
player1 = Person()
player1.talk()
player1.attack()