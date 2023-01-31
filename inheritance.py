# Child Class "IS A" parents class
# # teacher "IS A" person = this is correct
# dog "IS A" person = this is incorrect

# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
        
#     def walk(self):
#         print(f"{self.name} is walking.")
        
# class Teacher(Person):
#     def __init__(self, name, address, designation):
#         super().__init__(name, address)
#         self.designation = designation
        
    
#     def teach(self):
#         print(f"{self.name} is teaching. ")
        
# class Student(Person):
#     def __init__(self, name, address, roll_number):
#         super().__init__(name, address)
#         self.roll = roll_number
        
#     def walk(self):
#         super().walk()
#         print(f"{self.name} is running. ")   
      
      
        
        
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
        
# class Person(User):
#     def __init__(self, username, password, name, address):
#         super().__init__(username, password)
#         self.name = name
#         self.address = address
        
#     def profile(self):
#         print(f"Name:{self.name}")
#         print(f"Address:{self.address}")
#         print(f"Username:{self.username}")
        
# class Student(Person):
#     def __init__(self, username, name, password, address, roll_number):
#         super().__init__(name, username, address, password, )
#         self.roll_number = roll_number
        
#     def profile(self):
#         super().profile()
#         print(f"Roll_number:{self.roll_number}")
    
    
# class Teacher(Person):
#     def __init__(self, username, password, name, address, designation):
#         super().__init__(username, password,name, address)
#         self.designation = designation
        
#     def profile(self):
#         super().profile()
#         print(f"Designation:{self.designation}")
        
# p = Person("hari", "qwerty", "ram", "ktm")
# p.profile()

# print("_"*10)

# s = Student("azay", "zxcv", "hem", "qwe", "7")
# s.profile()

# print("_"*45)

# t = Teacher("shyam", "add", "sub", "azay", "yujk")
# t.profile()


    
        
        
        
      
        
        
        
# t = Teacher("Ram", "Ktm", "prof")
# t.walk()
# t.teach()

# s = Student("hari", "ktm", "prof")
# s.walk()

class ProductPriceError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        
    @property