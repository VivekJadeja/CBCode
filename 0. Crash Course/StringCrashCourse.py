a = [[]] * 3 # "a" actually just has one inner list but referenced 3 times
print(a)
a[0].append("value")
print(a)

n = [[] for _ in range (3)]
n[0].append("value")
print(n)

a = [1]
print(a)
n = a
print(n)
n[0] = 2
print(n)

random_list = ["Joe", "Steve", "Ann", "Bnn"]

sorted_list = sorted(random_list) # [1,2,3,4,5]
print(sorted_list)
reverse_list = sorted(random_list, reverse = True) # [5,4,3,2,1]
print(reverse_list)

# One can also sort lists with a custom key using lambda.
class Person:
   def __init__(self, name, age):
      self.age = age
      self.name = name

   # Provides a string representation of this object.
   def __repr__(self):
      return repr((self.name, self.age))

bob = Person("Bob", 14)
sam = Person("Sam", 12)
ann = Person("Ann", 16)

people = [bob, sam, ann]
print(people)
# Sort it by their first name.
people.sort(key=lambda x: x.name) # [("Ann", 16), ("Bob", 14), ("Sam", 12)]
print(people)
people.sort(key=lambda x: x.age) # [("Sam", 12), ("Bob", 14), ("Ann", 16)]
print(people)