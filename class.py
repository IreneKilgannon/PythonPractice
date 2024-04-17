#class Dog:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#    
#    def sit(self):
#        print(f'{self.name} is now sitting')
#
#    def roll_over(self):
#        print(f'{self.name} rolled over')
#
#my_dog = Dog('Willie', 5)
#
#
#print(f"My dog's name is {my_dog.name}.")
#print(f"My dog's age is {my_dog.age}.")
#
#my_dog.name
#my_dog.sit()
#my_dog.roll_over()

class Nameofclass:
    name = ''
    last = ''
    def getfullname(self):
        return self.name + ' ' + self.last


inst = Nameofclass()
inst2 = Nameofclass()
person = inst

inst.name = 'irene'
inst.last = 'test'
person = inst

print(person.name)


print(person.getfullname())



