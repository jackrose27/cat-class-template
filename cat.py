class Cat():
    def __init__(self, name = 'unknown', age = 0):
        self.name = name
        self.age = age

    def speak(self):
        return('Meow')

stella = Cat()
stella.name = "Stella"
stella.age = 7
stella.speak()


garfield = Cat()
garfield.name = 'garfield'
garfield.age = 50
garfield.speak()


        



