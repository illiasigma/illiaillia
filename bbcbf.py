class Animal:

def __init__(self, name, age):

self.name = name

self.age = age

def speak(self):

print(f"{self.name} говорить!")

def get_info(self):

print(f"Тварина: {self.name}, вік: {self.age} років")

class Dog(Animal):

def __init__(self, name, age, breed):

super().__init__(name, age)

self.breed = breed

def speak(self):

print(f"{self.name} гавкає!")

def get_info(self):

super().get_info()

print(f"Порода собаки: {self.breed}")

class Cat(Animal):

def __init__(self, name, age, color):

super().__init__(name, age)

self.color = color

def speak(self):

print(f"{self.name} мявкає!")

def get_info(self):

super().get_info()

print(f"Колір кота: {self.color}")

dog = Dog("Шарик", 5, "Овчарка")

cat = Cat("Мурка", 3, "Сіра")

dog.get_info()

dog.speak()

cat.get_info()

cat.speak()