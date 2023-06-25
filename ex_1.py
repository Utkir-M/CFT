class Animal:
    def say(self):
        raise NotImplementedError
    def eat(self):
        return "вкусно!"

class Cat:
    def say(self):
        return "Мяяу! "
    
class Dog:
    def say(self):
        return 'Гав! '
    
class CatDog(Cat, Dog):
    def eat(self):
        return "Я не могу есть."
    
catdog = CatDog()

print(f'{catdog.say()} {catdog.eat()}')