class pet:
    def __init__(self, name, species, age):
        self.__name = name
        self.__type = species
        self.__age = age


    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, species):
         self.__type = species

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__type

    def get_age(self):
        return self.__age

name = input('whats your pets name?')
animal_type = input('what type of animal is your pet?')
age = input('how old is your pet?')
pet1 = pet(name, animal_type, age)

print('/nName:',pet1.get_name())
print('animal type:',pet1.get_animal_type())
print('age:',pet1.get_age())
