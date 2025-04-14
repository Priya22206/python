# In Python, a class is a blueprint for creating objects (instances). 
# It defines a set of attributes (variables) and methods (functions) that the objects created from the class will have.
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class xyz:
    a=23

o = xyz()
print(o.a)

# The __init__() function is called automatically every time the class is being used to create a new object.

class person:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country
        
p1 = person('Priya',23, 'India')
p2 = person('Ravi',32, 'India')

print(p1.name)
print(p2.age, p2.country)

# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} {self.age} "    

p1 = Person("John", 36)

print(p1)

# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# You can modify properties on objects like this

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1.age)

p1.age = 40 # Modify age

print(p1.age)

# You can delete properties on objects by using the del keyword:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age # Deleted age attribute

print(p1.age)

del p1      # Delete 

# Class can define without set of attributes (variables) and methods (functions) with pass statement
class Person:
	pass



