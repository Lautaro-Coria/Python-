#ejemplo de clase con dos objetos: 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# Call the bark method
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!

#Aquí se muestran ejemplos de atributos de instancia y de clase, y cómo acceder a ellos desde los objetos:
class Dog:
    species = "French Bulldog" # Class attribute

    def __init__(self, name):
        self.name = name # Instance attribute

print(Dog.species) # French Bulldog

dog1 = Dog("Jack")
print(dog1.name)    # Jack
print(dog1.species) # French Bulldog

dog2 = Dog("Tom")
print(dog2.name)    # Tom
print(dog2.species) # French Bulldog

#Los coches son otro buen ejemplo, ya que todos los coches tienen un modelo y un color:
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.model) # Toyota Corolla
print(car_2.model) # Lamborghini Revuelto

print(car_1.color) # red
print(car_2.color) # green

#ómo puedes definir tus propios métodos __len__(), __str__(), y __eq__()especiales para facilitar el trabajo con objetos creados a partir de la Bookclase:
class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

   def __len__(self):
       return self.pages

   def __str__(self):
       return f"'{self.title}' has {self.pages} pages"

   def __eq__(self, other):
       return self.pages == other.pages
  
book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1)) # 420
print(len(book2)) # 420
print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # 'Be Your Own Start' has 420 pages
print(book1 == book2) # True