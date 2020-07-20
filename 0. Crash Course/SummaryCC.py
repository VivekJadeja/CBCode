class Dog:
    #Class Attribute; Basically applies to all objects of the class
    species = 'mammal'

    #Constructor/Initializer
    def __init__(self, name, age):
        #Underscores for attributes indicate private variables
        #There are no true private variables, because all this does
        #is change the variable name from the arugment name
        #so that it kind of obfuscates/makes a difference
        #in the two names. But it does not become truly private
        #and inaccessible. ex: self._name = name, self._age = age
        self.name = name
        self.age = age

    #Instance Method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    #Instance Method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

my_dog = Dog("Snoopy", 8) # Object of Dog class
print(my_dog.name)
print(my_dog.age)

# Calling our instance methods
print(my_dog.description())
print(my_dog.speak("woof"))

#Changing an attribute
my_dog.age = 9
print(my_dog.age)

#Inheriting a parent class
#class ChilcClass(ParentClass):
class Beagle(Dog):
    def run(self, speed):
        return "{}, the Beagle, runs {}.".format(self.name, speed)

snoopy = Beagle("Snoopy", 8)
print(snoopy.description())

print(snoopy.run("fast"))
