class Person:
    def __init__ (self, firstName, secondName, age):

        self.firstName = firstName
        self.secondName = secondName
        self.age = age

    @staticmethod
    def isabove30(age):
        return age>30

    def walk (self):
        return (f"{self.firstName} is walking...") 
    
    def work (self):
        return (f"{self.firstName} is working...")
    
    def __str__(self):
        return (f"{self.firstName}, {self.secondName}, Age = {self.age}")

class Student(Person):

    def __init__ (self, firstName, secondName, age, major):

        super().__init__ (firstName, secondName, age)
        self.major= major
        self.__grade = None
    
    def work (self):
        return (f"{self.name}, is studying....")
    
    @property
    def grade (self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        self.__grade = value
        return self.__grade
    
    def __str__(self):
        return (f"{self.firstName}, {self.secondName}, Age = {self.age} major = {self.major}")
    
class Citizen(Person):
        
    def register(self):
        return (f"{self.firstName}, {self.secondName} has been registered")
        
s1 = Student("Peter", "Ngure", 30, "Computer simulations")
print (s1)
c1 = Citizen("Anthony", "Andrew", 45)
print (c1)
s1.grade = 96
print(s1.grade)