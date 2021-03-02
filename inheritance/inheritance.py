class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working ....")

    def __str__ (self):
        return f"{self.name} , {self.age}, {self.salary}"

class SoftwareEngineer(Employee):
    def __init__ (self, name, age,salary, level):
        super().__init__(name, age, salary)
        self.level=level
    
    def debug (self):
        print(f"{self.name} is debugging...")

    def work(self):
        print(f"{self.name} is coding ....")
    
    def __str__ (self):
        return f"{self.name} , {self.age}, {self.salary}, {self.level}"


class Designer (Employee):
    
    def draw (self):
        print(f"{self.name} is drawing...")
    def work(self):
        print(f"{self.name} is designing ....")

se = SoftwareEngineer("max", 20, 2000, "Junior")
d1 = Designer("Newton", 30, 3000)
print (se)
print (d1)