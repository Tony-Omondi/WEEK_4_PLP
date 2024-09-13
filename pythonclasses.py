class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}. I am {self.age} years old and I am {self.gender}.")
person = Person(name="Tony Otieno", age=19, gender="Male")


person.introduce()
